import React, { useState, useRef, useEffect } from 'react';
import { 
  Camera, Upload, Sparkles, RefreshCw, Download, 
  CheckCircle2, AlertTriangle, ShieldAlert, ArrowRight,
  Eye, FlipHorizontal, X, FileText
} from 'lucide-react';
import confetti from 'canvas-confetti';

export default function PestDetector({ onDetectionComplete, initialSample }) {
  const [mode, setMode] = useState('camera'); // 'camera', 'upload', 'samples'
  
  // Camera state
  const videoRef = useRef(null);
  const streamRef = useRef(null);
  const [cameraActive, setCameraActive] = useState(false);
  const [cameraFacing, setCameraFacing] = useState('environment'); // 'user' or 'environment'
  const [cameraError, setCameraError] = useState(null);
  const [capturedImageB64, setCapturedImageB64] = useState(null);

  // File Upload state
  const [uploadedFile, setUploadedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);

  // Samples state
  const [samples, setSamples] = useState([]);
  const [selectedSample, setSelectedSample] = useState(null);

  // Detection state
  const [loading, setLoading] = useState(false);
  const [detectionResult, setDetectionResult] = useState(null);
  const [selectedCrop, setSelectedCrop] = useState('General Field Crop');
  const [activeResultTab, setActiveResultTab] = useState('annotated'); // 'annotated' or 'original'

  // Fetch samples on mount
  useEffect(() => {
    fetch('/api/samples')
      .then(res => res.json())
      .then(data => {
        if (data.samples) {
          setSamples(data.samples);
          if (initialSample) {
            const found = data.samples.find(s => s.filename.includes(initialSample));
            if (found) {
              setMode('samples');
              handleSelectSample(found);
            }
          }
        }
      })
      .catch(err => console.error('Error fetching samples:', err));
  }, [initialSample]);

  // Camera Management
  const startCamera = async (facing = cameraFacing) => {
    stopCamera();
    setCameraError(null);
    try {
      const constraints = {
        video: {
          facingMode: facing,
          width: { ideal: 1280 },
          height: { ideal: 720 }
        }
      };
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
      setCameraActive(true);
    } catch (err) {
      console.error('Camera error:', err);
      setCameraError('Camera access was denied or is not supported. Please allow camera permissions in your browser or use the Upload option.');
      setCameraActive(false);
    }
  };

  const stopCamera = () => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach(track => track.stop());
      streamRef.current = null;
    }
    setCameraActive(false);
  };

  // Flip camera between front and rear on mobile
  const toggleCameraFacing = () => {
    const nextFacing = cameraFacing === 'environment' ? 'user' : 'environment';
    setCameraFacing(nextFacing);
    if (cameraActive) {
      startCamera(nextFacing);
    }
  };

  // Capture snapshot from video
  const capturePhoto = () => {
    if (!videoRef.current) return;
    const canvas = document.createElement('canvas');
    canvas.width = videoRef.current.videoWidth || 640;
    canvas.height = videoRef.current.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg', 0.92);
    setCapturedImageB64(dataUrl);
    setPreviewUrl(dataUrl);
    stopCamera();
  };

  const retakePhoto = () => {
    setCapturedImageB64(null);
    setPreviewUrl(null);
    setDetectionResult(null);
    startCamera(cameraFacing);
  };

  // Handle Tab Change
  const handleModeChange = (newMode) => {
    setMode(newMode);
    setDetectionResult(null);
    if (newMode === 'camera') {
      setPreviewUrl(capturedImageB64);
      if (!capturedImageB64) {
        startCamera(cameraFacing);
      }
    } else {
      stopCamera();
      if (newMode === 'upload') {
        setPreviewUrl(uploadedFile ? URL.createObjectURL(uploadedFile) : null);
      } else if (newMode === 'samples') {
        setPreviewUrl(selectedSample ? selectedSample.preview_url : null);
      }
    }
  };

  // Stop camera when unmounting
  useEffect(() => {
    return () => stopCamera();
  }, []);

  // File Upload Handlers
  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file) {
      setUploadedFile(file);
      setPreviewUrl(URL.createObjectURL(file));
      setDetectionResult(null);
    }
  };

  const clearFile = () => {
    setUploadedFile(null);
    setPreviewUrl(null);
    setDetectionResult(null);
  };

  // Sample Selection Handler
  const handleSelectSample = (sample) => {
    setSelectedSample(sample);
    setPreviewUrl(sample.preview_url);
    setDetectionResult(null);
  };

  // Run AI Pest Diagnosis
  const runDiagnosis = async () => {
    setLoading(true);
    setDetectionResult(null);

    const formData = new FormData();
    formData.append('crop', selectedCrop);
    formData.append('conf', '0.25');

    if (mode === 'upload' && uploadedFile) {
      formData.append('file', uploadedFile);
    } else if (mode === 'camera' && capturedImageB64) {
      formData.append('image_base64', capturedImageB64);
    } else if (mode === 'samples' && selectedSample) {
      formData.append('image_base64', selectedSample.preview_url);
    } else {
      alert('Please provide an image first!');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch('/api/detect', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Diagnosis failed.');
      }

      const data = await response.json();
      setDetectionResult(data);

      if (data.num_detections === 0) {
        confetti({ particleCount: 40, spread: 60, origin: { y: 0.6 } });
      }

      if (onDetectionComplete) {
        onDetectionComplete({
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          crop: selectedCrop,
          num_detections: data.num_detections,
          class_counts: data.class_counts,
          max_confidence: data.max_confidence_pct / 100,
          annotated_image: data.annotated_image,
        });
      }
    } catch (err) {
      alert('Error running detection: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="max-w-6xl mx-auto px-4 py-8">
      
      {/* Title Header */}
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 bg-emerald-100 text-emerald-800 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Camera & Upload Scanner</span>
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 mb-2">
          Inspect Crop Foliage
        </h1>
        <p className="text-sm sm:text-base font-medium text-slate-600">
          Point your camera at a crop leaf or upload an image to identify pests and get immediate organic field remedies.
        </p>
      </div>

      {/* Mode Switcher Tabs */}
      <div className="flex flex-wrap items-center gap-3 mb-6">
        <button
          onClick={() => handleModeChange('camera')}
          className={`flex items-center gap-2 px-5 py-2.5 rounded-2xl font-extrabold text-sm neo-border-sm transition-all cursor-pointer ${
            mode === 'camera'
              ? 'bg-emerald-400 text-slate-900 neo-shadow -translate-y-0.5'
              : 'bg-white text-slate-700 hover:bg-slate-50'
          }`}
        >
          <Camera className="w-4 h-4" />
          <span>Take Photo with Camera</span>
        </button>

        <button
          onClick={() => handleModeChange('upload')}
          className={`flex items-center gap-2 px-5 py-2.5 rounded-2xl font-extrabold text-sm neo-border-sm transition-all cursor-pointer ${
            mode === 'upload'
              ? 'bg-emerald-400 text-slate-900 neo-shadow -translate-y-0.5'
              : 'bg-white text-slate-700 hover:bg-slate-50'
          }`}
        >
          <Upload className="w-4 h-4" />
          <span>Upload Image from Device</span>
        </button>

        <button
          onClick={() => handleModeChange('samples')}
          className={`flex items-center gap-2 px-5 py-2.5 rounded-2xl font-extrabold text-sm neo-border-sm transition-all cursor-pointer ${
            mode === 'samples'
              ? 'bg-emerald-400 text-slate-900 neo-shadow -translate-y-0.5'
              : 'bg-white text-slate-700 hover:bg-slate-50'
          }`}
        >
          <span>🌾 Use a Sample Photo</span>
        </button>
      </div>

      {/* Main Workspace Card */}
      <div className="neo-card p-6 sm:p-8 mb-8">
        
        {/* --- CAMERA MODE --- */}
        {mode === 'camera' && (
          <div>
            {!capturedImageB64 ? (
              <div className="relative rounded-2xl neo-border-sm overflow-hidden bg-slate-900 max-w-xl mx-auto neo-shadow">
                {cameraError ? (
                  <div className="p-8 text-center text-white">
                    <AlertTriangle className="w-12 h-12 text-amber-400 mx-auto mb-3" />
                    <p className="text-sm font-bold mb-4">{cameraError}</p>
                    <button
                      onClick={() => handleModeChange('upload')}
                      className="bg-emerald-500 text-white font-extrabold px-5 py-2.5 rounded-xl neo-btn text-xs"
                    >
                      Switch to File Upload
                    </button>
                  </div>
                ) : (
                  <>
                    <video
                      ref={videoRef}
                      autoPlay
                      playsInline
                      muted
                      className="w-full h-72 sm:h-96 object-cover"
                    />

                    {/* Viewfinder crosshairs */}
                    <div className="absolute inset-8 border-2 border-dashed border-white/60 rounded-xl pointer-events-none flex items-center justify-center">
                      <span className="text-xs font-extrabold bg-slate-900/80 text-white px-3 py-1 rounded-full neo-border-sm">
                        Center leaf or insect here
                      </span>
                    </div>

                    {/* Controls Bar over video */}
                    <div className="absolute bottom-4 inset-x-4 flex items-center justify-between gap-4">
                      <button
                        onClick={toggleCameraFacing}
                        className="bg-white/90 hover:bg-white text-slate-800 p-3 rounded-2xl neo-border-sm neo-shadow-sm flex items-center gap-2 text-xs font-extrabold cursor-pointer"
                        title="Flip Camera"
                      >
                        <FlipHorizontal className="w-4 h-4" />
                        <span className="hidden sm:inline">Flip</span>
                      </button>

                      <button
                        onClick={capturePhoto}
                        className="bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold px-6 py-3 rounded-2xl neo-btn flex items-center gap-2 text-sm shadow-lg cursor-pointer"
                      >
                        <Camera className="w-5 h-5" />
                        <span>Take Photo</span>
                      </button>

                      <div className="w-10"></div>
                    </div>
                  </>
                )}
              </div>
            ) : (
              /* Captured preview with Retake */
              <div className="max-w-xl mx-auto text-center">
                <div className="rounded-2xl neo-border-sm overflow-hidden neo-shadow mb-4">
                  <img src={capturedImageB64} alt="Captured crop" className="w-full h-72 sm:h-96 object-cover" />
                </div>
                <div className="flex justify-center gap-4">
                  <button
                    onClick={retakePhoto}
                    className="flex items-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold px-5 py-2.5 rounded-xl neo-btn text-xs cursor-pointer"
                  >
                    <RefreshCw className="w-4 h-4" />
                    <span>Retake Photo</span>
                  </button>
                </div>
              </div>
            )}
          </div>
        )}

        {/* --- UPLOAD MODE --- */}
        {mode === 'upload' && (
          <div>
            {!previewUrl ? (
              <label className="max-w-xl mx-auto border-2 border-dashed border-slate-400 hover:border-slate-800 rounded-3xl p-10 flex flex-col items-center justify-center cursor-pointer bg-slate-50 hover:bg-emerald-50/50 transition-all neo-shadow-sm block text-center">
                <input
                  type="file"
                  accept="image/png,image/jpeg,image/jpg,image/webp"
                  onChange={handleFileUpload}
                  className="hidden"
                />
                <div className="w-14 h-14 rounded-2xl neo-border-sm bg-rose-200 flex items-center justify-center mb-4 neo-shadow-sm">
                  <Upload className="w-7 h-7 text-slate-800" />
                </div>
                <h3 className="font-extrabold text-slate-800 text-lg mb-1">
                  Upload Leaf Photo
                </h3>
                <p className="text-xs font-medium text-slate-500 mb-4">
                  Drag and drop or click to browse (JPG, JPEG, PNG, WEBP)
                </p>
                <span className="bg-emerald-500 text-white font-extrabold text-xs px-4 py-2 rounded-xl neo-btn">
                  Choose from Gallery
                </span>
              </label>
            ) : (
              <div className="max-w-xl mx-auto text-center">
                <div className="relative rounded-2xl neo-border-sm overflow-hidden neo-shadow mb-4">
                  <img src={previewUrl} alt="Uploaded crop" className="w-full h-72 sm:h-96 object-cover" />
                  <button
                    onClick={clearFile}
                    className="absolute top-3 right-3 bg-white text-slate-800 p-2 rounded-xl neo-border-sm neo-shadow-sm hover:bg-rose-100 cursor-pointer"
                    title="Remove Photo"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
                <button
                  onClick={clearFile}
                  className="bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold px-5 py-2.5 rounded-xl neo-btn text-xs cursor-pointer"
                >
                  Change Image
                </button>
              </div>
            )}
          </div>
        )}

        {/* --- SAMPLES MODE --- */}
        {mode === 'samples' && (
          <div>
            <p className="text-xs font-bold text-slate-500 text-center mb-4">
              Select one of our verified agricultural sample images to test the model:
            </p>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 max-w-2xl mx-auto mb-6">
              {samples.map((s, idx) => {
                const isSelected = selectedSample?.filename === s.filename;
                return (
                  <div
                    key={idx}
                    onClick={() => handleSelectSample(s)}
                    className={`rounded-2xl p-2 cursor-pointer neo-border-sm transition-all text-center ${
                      isSelected ? 'bg-emerald-200 neo-shadow -translate-y-1' : 'bg-white hover:bg-slate-50'
                    }`}
                  >
                    <img src={s.preview_url} alt={s.title} className="w-full h-24 object-cover rounded-xl mb-2 neo-border-sm" />
                    <p className="text-xs font-extrabold text-slate-800 truncate">{s.title}</p>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Action Button Row */}
        {previewUrl && (
          <div className="mt-8 pt-6 border-t-2 border-slate-100 max-w-xl mx-auto">
            <div className="mb-4">
              <label className="block text-xs font-extrabold text-slate-700 mb-1.5">
                Crop Type (Optional):
              </label>
              <select
                value={selectedCrop}
                onChange={(e) => setSelectedCrop(e.target.value)}
                className="w-full neo-border-sm rounded-xl px-4 py-2.5 text-sm font-bold bg-white text-slate-800 neo-shadow-sm focus:outline-none"
              >
                <option value="General Field Crop">General Field Crop</option>
                <option value="Rice">Rice (धान / चावल)</option>
                <option value="Wheat">Wheat (गेहूं)</option>
                <option value="Cotton">Cotton (कपास)</option>
                <option value="Maize">Maize (मक्का)</option>
                <option value="Tomato">Tomato (टमाटर)</option>
                <option value="Soybean">Soybean (सोयाबीन)</option>
                <option value="Mango">Mango (आम)</option>
                <option value="Citrus">Citrus (नींबू संतरा)</option>
              </select>
            </div>

            <button
              onClick={runDiagnosis}
              disabled={loading}
              className="w-full flex items-center justify-center gap-2 bg-emerald-500 hover:bg-emerald-600 disabled:bg-slate-300 text-white font-extrabold text-base py-3.5 rounded-2xl neo-btn cursor-pointer"
            >
              {loading ? (
                <>
                  <RefreshCw className="w-5 h-5 animate-spin" />
                  <span>Scanning Leaf with Vision Model...</span>
                </>
              ) : (
                <>
                  <Sparkles className="w-5 h-5" />
                  <span>Run Pest Diagnosis</span>
                </>
              )}
            </button>
          </div>
        )}

      </div>

      {/* =================================================================== */}
      {/* DETECTION RESULTS SECTION                                          */}
      {/* =================================================================== */}
      {detectionResult && (
        <div className="neo-card p-6 sm:p-8 neo-shadow-lg animate-in fade-in duration-300">
          
          {/* Verdict Banner */}
          {detectionResult.num_detections === 0 ? (
            <div className="bg-emerald-100 neo-border rounded-2xl p-6 mb-8 flex items-center gap-4 neo-shadow-sm">
              <div className="w-14 h-14 rounded-2xl neo-border-sm bg-white flex items-center justify-center text-3xl neo-shadow-sm shrink-0">
                ✅
              </div>
              <div>
                <h3 className="text-xl sm:text-2xl font-extrabold text-emerald-900 mb-1">
                  Great News! No Pests Detected
                </h3>
                <p className="text-xs sm:text-sm font-medium text-emerald-800">
                  Our agricultural vision scanner analyzed your photo and found no signs of common crop pests. Your foliage looks healthy and clean!
                </p>
              </div>
            </div>
          ) : (
            <div className="bg-rose-100 neo-border rounded-2xl p-6 mb-8 neo-shadow-sm">
              <div className="flex flex-wrap items-start justify-between gap-4">
                <div>
                  <div className="inline-block bg-white text-rose-700 neo-border-sm font-extrabold text-xs px-3 py-1 rounded-full neo-shadow-sm mb-2">
                    ⚠️ {detectionResult.severity.level}
                  </div>
                  <h3 className="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-1">
                    {detectionResult.num_detections} Pest Specimen(s) Located
                  </h3>
                  <p className="text-xs sm:text-sm font-medium text-slate-700">
                    {detectionResult.severity.description}
                  </p>
                </div>
                <div className="text-right">
                  <div className="text-xs font-bold text-slate-600">Match Certainty</div>
                  <div className="text-3xl font-extrabold text-emerald-600">
                    {detectionResult.max_confidence_pct}%
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Photo Inspection Tabs */}
          <div className="mb-8">
            <div className="flex gap-2 mb-4">
              <button
                onClick={() => setActiveResultTab('annotated')}
                className={`px-4 py-2 rounded-xl font-extrabold text-xs sm:text-sm neo-border-sm cursor-pointer ${
                  activeResultTab === 'annotated'
                    ? 'bg-emerald-300 text-slate-900 neo-shadow-sm'
                    : 'bg-white text-slate-600 hover:bg-slate-50'
                }`}
              >
                🎯 Marked Pests (Bounding Boxes)
              </button>
              <button
                onClick={() => setActiveResultTab('original')}
                className={`px-4 py-2 rounded-xl font-extrabold text-xs sm:text-sm neo-border-sm cursor-pointer ${
                  activeResultTab === 'original'
                    ? 'bg-emerald-300 text-slate-900 neo-shadow-sm'
                    : 'bg-white text-slate-600 hover:bg-slate-50'
                }`}
              >
                🖼️ Original Photo
              </button>
            </div>

            <div className="max-w-2xl mx-auto rounded-2xl neo-border overflow-hidden neo-shadow">
              <img
                src={activeResultTab === 'annotated' ? detectionResult.annotated_image : detectionResult.original_image}
                alt="Diagnosis view"
                className="w-full max-h-[500px] object-contain bg-slate-950"
              />
            </div>
          </div>

          {/* Practical 3-Pillar Remedies */}
          {detectionResult.num_detections > 0 && (
            <div className="mb-8">
              <h3 className="text-xl sm:text-2xl font-extrabold text-slate-900 mb-4">
                🌾 Practical Field Remedies & Action Steps
              </h3>

              {Object.entries(detectionResult.remedies || {}).map(([pestName, rem], idx) => (
                <div key={idx} className="mb-6">
                  <div className="flex items-baseline gap-2 mb-2">
                    <h4 className="font-extrabold text-lg text-slate-900">
                      🐛 Care Protocol for {rem.common_name} {rem.hindi_name && `(${rem.hindi_name})`}
                    </h4>
                  </div>
                  <p className="text-xs font-medium text-slate-600 mb-4 italic">
                    How to spot: {rem.how_to_spot}
                  </p>

                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="bg-emerald-50 neo-border-sm rounded-2xl p-4 neo-shadow-sm">
                      <div className="w-8 h-8 rounded-lg neo-border-sm bg-emerald-200 flex items-center justify-center text-sm font-extrabold mb-2">
                        🌿
                      </div>
                      <h5 className="font-extrabold text-sm text-slate-900 mb-1">Organic Care</h5>
                      <p className="text-xs font-medium text-slate-700 whitespace-pre-line leading-relaxed">
                        {rem.prevention_organic}
                      </p>
                    </div>

                    <div className="bg-amber-50 neo-border-sm rounded-2xl p-4 neo-shadow-sm">
                      <div className="w-8 h-8 rounded-lg neo-border-sm bg-amber-200 flex items-center justify-center text-sm font-extrabold mb-2">
                        🐞
                      </div>
                      <h5 className="font-extrabold text-sm text-slate-900 mb-1">Natural Allies</h5>
                      <p className="text-xs font-medium text-slate-700 leading-relaxed">
                        {rem.natural_predators}
                      </p>
                    </div>

                    <div className="bg-sky-50 neo-border-sm rounded-2xl p-4 neo-shadow-sm">
                      <div className="w-8 h-8 rounded-lg neo-border-sm bg-sky-200 flex items-center justify-center text-sm font-extrabold mb-2">
                        🧪
                      </div>
                      <h5 className="font-extrabold text-sm text-slate-900 mb-1">Field Treatment</h5>
                      <p className="text-xs font-medium text-slate-700 leading-relaxed">
                        {rem.recommended_treatment}
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Download Buttons */}
          <div className="flex flex-wrap items-center gap-4 pt-6 border-t-2 border-slate-100">
            <a
              href={detectionResult.annotated_image}
              download="FasalMitra_Diagnosis.jpg"
              className="flex items-center gap-2 bg-sky-200 hover:bg-sky-300 text-slate-900 font-extrabold px-5 py-2.5 rounded-xl neo-btn text-xs sm:text-sm cursor-pointer"
            >
              <Download className="w-4 h-4" />
              <span>Download Marked Photo (JPEG)</span>
            </a>

            <button
              onClick={() => {
                setDetectionResult(null);
                setPreviewUrl(null);
                setCapturedImageB64(null);
                setUploadedFile(null);
                if (mode === 'camera') startCamera(cameraFacing);
              }}
              className="flex items-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold px-5 py-2.5 rounded-xl neo-btn text-xs sm:text-sm cursor-pointer"
            >
              <RefreshCw className="w-4 h-4" />
              <span>Scan Another Leaf</span>
            </button>
          </div>

        </div>
      )}

    </section>
  );
}
