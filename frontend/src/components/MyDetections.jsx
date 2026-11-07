import React from 'react';
import { Trash2, Download, Eye, Sparkles } from 'lucide-react';

export default function MyDetections({ history = [], onClearHistory, onStartDetection }) {
  return (
    <section className="max-w-6xl mx-auto px-4 py-8">
      
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-4 mb-8">
        <div>
          <div className="inline-flex items-center gap-2 bg-amber-200 text-slate-900 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
            <span>🕒 Session Audit Trail</span>
          </div>
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 mb-2">
            My Detections
          </h1>
          <p className="text-sm sm:text-base font-medium text-slate-600">
            Revisit crop photos and diagnoses made during your active session. Stored in-memory for your privacy.
          </p>
        </div>

        {history.length > 0 && (
          <button
            onClick={onClearHistory}
            className="flex items-center gap-2 bg-rose-200 hover:bg-rose-300 text-slate-900 font-extrabold text-xs sm:text-sm px-4 py-2.5 rounded-xl neo-btn cursor-pointer"
          >
            <Trash2 className="w-4 h-4" />
            <span>Clear History</span>
          </button>
        )}
      </div>

      {/* Empty State */}
      {history.length === 0 ? (
        <div className="neo-card p-12 sm:p-16 text-center max-w-xl mx-auto">
          <div className="w-16 h-16 rounded-2xl neo-border-sm bg-amber-200 flex items-center justify-center text-3xl neo-shadow-sm mx-auto mb-4">
            📋
          </div>
          <h3 className="text-2xl font-extrabold text-slate-900 mb-2">
            No Saved Detections Yet
          </h3>
          <p className="text-sm font-medium text-slate-600 mb-6">
            Any crop leaf diagnosis you run in the <b>Pest Detection</b> studio will appear here during your visit.
          </p>
          <button
            onClick={onStartDetection}
            className="bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold text-sm px-6 py-3 rounded-2xl neo-btn cursor-pointer inline-flex items-center gap-2"
          >
            <Sparkles className="w-4 h-4" />
            <span>Diagnose Your First Leaf</span>
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {history.map((item, idx) => {
            const isClean = item.num_detections === 0;
            const pestsTitle = Object.keys(item.class_counts || {}).join(', ') || 'No Pests (Healthy)';
            return (
              <div key={idx} className="neo-card p-6 flex flex-col justify-between">
                <div>
                  <div className="rounded-2xl neo-border-sm overflow-hidden mb-4 bg-slate-950">
                    <img
                      src={item.annotated_image}
                      alt="Crop Diagnosis"
                      className="w-full h-56 object-contain"
                    />
                  </div>

                  <div className="flex items-center justify-between gap-2 mb-2">
                    <span className={`text-xs font-extrabold px-3 py-1 rounded-full neo-border-sm ${
                      isClean ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800'
                    }`}>
                      {isClean ? '✅ Healthy Leaf' : `⚠️ ${item.num_detections} Pest(s) Located`}
                    </span>
                    <span className="text-xs font-bold text-slate-400">
                      {item.timestamp}
                    </span>
                  </div>

                  <h3 className="font-extrabold text-lg text-slate-900 mb-1">
                    {pestsTitle}
                  </h3>

                  <p className="text-xs font-bold text-emerald-700 mb-4">
                    🌾 Crop: {item.crop} &bull; Match Certainty: {Math.round(item.max_confidence * 100)}%
                  </p>
                </div>

                <div className="pt-3 border-t-2 border-slate-100">
                  <a
                    href={item.annotated_image}
                    download={`FasalMitra_Scan_${idx+1}.jpg`}
                    className="flex items-center justify-center gap-2 bg-sky-200 hover:bg-sky-300 text-slate-900 font-extrabold text-xs py-2 px-4 rounded-xl neo-btn cursor-pointer"
                  >
                    <Download className="w-3.5 h-3.5" />
                    <span>Download Photo</span>
                  </a>
                </div>
              </div>
            );
          })}
        </div>
      )}

    </section>
  );
}
