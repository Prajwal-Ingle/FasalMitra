import React from 'react';
import { ArrowRight, BookOpen, Camera, CheckCircle2 } from 'lucide-react';

export default function Hero({ onStartDetection, onExplorePests, onSampleClick }) {
  return (
    <section className="max-w-6xl mx-auto px-4 pt-6 pb-14">
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        {/* Left Column: Heading and Call to Action */}
        <div className="lg:col-span-7">
          
          {/* Pill Badge */}
          <div className="inline-flex items-center gap-2 bg-emerald-100 text-emerald-800 font-extrabold text-xs md:text-sm px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-4">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>AI-Powered Crop Pest Protection</span>
          </div>

          {/* Heading */}
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-slate-900 leading-[1.15] mb-5">
            Diagnose Any Crop,<br />
            <span className="text-emerald-500">Anytime,</span><br />
            Anywhere!
          </h1>

          {/* Subtitle */}
          <p className="text-base sm:text-lg font-medium text-slate-600 max-w-xl leading-relaxed mb-7">
            Protect your harvest from insect damage. Take a photo of a leaf or insect with your smartphone. 
            FasalMitra AI identifies pests in seconds, evaluates damage risk, and provides safe, organic field remedies.
          </p>

          {/* Buttons */}
          <div className="flex flex-wrap items-center gap-4">
            <button
              onClick={onStartDetection}
              className="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold text-base px-6 py-3.5 rounded-2xl neo-btn cursor-pointer"
            >
              <Camera className="w-5 h-5" />
              <span>Start Pest Diagnosis</span>
              <ArrowRight className="w-5 h-5" />
            </button>

            <button
              onClick={onExplorePests}
              className="flex items-center gap-2 bg-sky-200 hover:bg-sky-300 text-slate-900 font-extrabold text-base px-6 py-3.5 rounded-2xl neo-btn cursor-pointer"
            >
              <BookOpen className="w-5 h-5" />
              <span>Browse Crop Pests</span>
            </button>
          </div>

          {/* Quick Perks */}
          <div className="flex flex-wrap items-center gap-4 mt-6 text-xs sm:text-sm font-bold text-slate-600">
            <span className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
              100% Free for All Farmers
            </span>
            <span className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
              Direct Smartphone Camera Support
            </span>
            <span className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-emerald-600" />
              Zero Photos Saved to Cloud
            </span>
          </div>

        </div>

        {/* Right Column: Interactive Hero Card (Exact replica of Image 1 right card, 100% Agricultural!) */}
        <div className="lg:col-span-5 relative">
          
          <div className="relative mx-auto max-w-md bg-white neo-border rounded-3xl neo-shadow-lg p-6 sm:p-7">
            
            {/* Corner Decorative Badges */}
            <div className="absolute -top-3.5 -right-3.5 w-11 h-11 rounded-2xl neo-border-sm bg-rose-200 flex items-center justify-center text-xl neo-shadow-sm rotate-6">
              🎯
            </div>
            <div className="absolute -bottom-3.5 -right-3.5 w-11 h-11 rounded-full neo-border-sm bg-emerald-200 flex items-center justify-center text-xl neo-shadow-sm -rotate-6">
              ⭐
            </div>
            <div className="absolute -bottom-3.5 -left-3.5 w-11 h-11 rounded-2xl neo-border-sm bg-indigo-200 flex items-center justify-center text-xl neo-shadow-sm rotate-12">
              🌾
            </div>

            {/* Inner Content */}
            <div className="flex items-center gap-3.5 mb-5">
              <div className="w-12 h-12 rounded-2xl neo-border-sm bg-sky-200 flex items-center justify-center text-2xl neo-shadow-sm">
                🔍
              </div>
              <div>
                <h3 className="font-extrabold text-slate-800 text-lg">Paddy Leaf Health Scan</h3>
                <p className="text-xs font-bold text-slate-500">Rice (Oryza sativa) • Active Tillering</p>
              </div>
            </div>

            {/* Progress Section */}
            <div className="mb-6">
              <div className="flex justify-between text-xs font-bold text-slate-600 mb-1.5">
                <span>Diagnosis Certainty</span>
                <span className="text-emerald-600">94%</span>
              </div>
              <div className="w-full h-3.5 bg-slate-100 rounded-full neo-border-sm overflow-hidden p-0.5">
                <div className="h-full bg-emerald-500 rounded-full transition-all duration-500" style={{ width: '94%' }}></div>
              </div>
            </div>

            {/* Action inside card */}
            <button
              onClick={onSampleClick}
              className="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold py-3 px-4 rounded-xl neo-btn cursor-pointer flex items-center justify-center gap-2 text-sm"
            >
              <Camera className="w-4 h-4" />
              <span>Test with a Sample Leaf Photo</span>
            </button>

          </div>

        </div>

      </div>
    </section>
  );
}
