import React from 'react';
import { ArrowRight, Check, BookOpen, Camera } from 'lucide-react';

export default function FooterCTA({ onStartDetection, onExploreKnowledge }) {
  return (
    <section className="bg-sky-100 border-t-[2.5px] border-b-[2.5px] border-slate-800 py-16 px-4 mt-12">
      <div className="max-w-3xl mx-auto">
        <div className="bg-white neo-border rounded-3xl neo-shadow-lg p-8 sm:p-12 text-center">
          
          <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 mb-3">
            Ready to Protect Your Crops Today?
          </h2>

          <p className="text-sm sm:text-base font-medium text-slate-600 max-w-lg mx-auto mb-8">
            Join thousands of growers across the country detecting pests early and safeguarding their harvest. Start a free crop diagnosis right now in your browser!
          </p>

          {/* Action Buttons */}
          <div className="flex flex-wrap items-center justify-center gap-4 mb-6">
            <button
              onClick={onStartDetection}
              className="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold text-base px-6 py-3.5 rounded-2xl neo-btn cursor-pointer"
            >
              <Camera className="w-5 h-5" />
              <span>Start Free Diagnosis</span>
              <ArrowRight className="w-5 h-5" />
            </button>

            <button
              onClick={onExploreKnowledge}
              className="flex items-center gap-2 bg-sky-200 hover:bg-sky-300 text-slate-900 font-extrabold text-base px-6 py-3.5 rounded-2xl neo-btn cursor-pointer"
            >
              <BookOpen className="w-5 h-5" />
              <span>Explore Pest Directory</span>
            </button>
          </div>

          {/* Perks */}
          <div className="flex flex-wrap items-center justify-center gap-4 sm:gap-6 text-xs sm:text-sm font-bold text-slate-600">
            <span className="flex items-center gap-1.5">
              <Check className="w-4 h-4 text-emerald-600 stroke-[3]" />
              100% Free Forever
            </span>
            <span className="flex items-center gap-1.5">
              <Check className="w-4 h-4 text-emerald-600 stroke-[3]" />
              No Registration or Login
            </span>
            <span className="flex items-center gap-1.5">
              <Check className="w-4 h-4 text-emerald-600 stroke-[3]" />
              Zero Photos Stored on Cloud
            </span>
          </div>

        </div>
      </div>
    </section>
  );
}
