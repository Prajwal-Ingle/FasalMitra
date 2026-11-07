import React from 'react';
import { Shield, Zap, Leaf, IndianRupee, Info } from 'lucide-react';

export default function AboutSection() {
  return (
    <section className="max-w-6xl mx-auto px-4 py-8">
      
      {/* Header */}
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 bg-pink-200 text-slate-900 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          <span>🌾 About FasalMitra AI</span>
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 mb-2">
          Farmer's Trusted Crop Friend
        </h1>
        <p className="text-sm sm:text-base font-medium text-slate-600">
          Supporting growers with instant, private, and accessible pest diagnosis right in the field.
        </p>
      </div>

      {/* Mission Banner */}
      <div className="neo-card p-8 sm:p-10 mb-8 neo-shadow-lg">
        <div className="flex items-center gap-3.5 mb-4">
          <div className="w-12 h-12 rounded-2xl neo-border-sm bg-pink-200 flex items-center justify-center text-2xl neo-shadow-sm">
            🌾
          </div>
          <div>
            <h2 className="text-2xl font-extrabold text-slate-900">
              Empowering Every Farmer with Instant AI Care
            </h2>
            <p className="text-xs font-bold text-emerald-600">FasalMitra AI (फसल मित्र)</p>
          </div>
        </div>

        <p className="text-sm sm:text-base font-medium text-slate-700 leading-relaxed mb-4">
          <b>FasalMitra</b> means <i>"Farmer's Friend"</i>. Our mission is to put expert agricultural pest diagnosis directly into the hands of every farmer. By simply taking a photo with a smartphone, growers can identify crop pests early, protect their harvests, and avoid expensive or unnecessary chemical sprays.
        </p>
      </div>

      {/* 4 Benefit Cards */}
      <h3 className="text-2xl font-extrabold text-slate-900 mb-4">
        Why Farmers Trust FasalMitra
      </h3>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="neo-card p-6">
          <div className="w-12 h-12 rounded-xl neo-border-sm bg-emerald-200 flex items-center justify-center mb-3 neo-shadow-sm">
            <Zap className="w-6 h-6 text-slate-800" />
          </div>
          <h4 className="font-extrabold text-lg text-slate-900 mb-1">
            Instant Field Diagnosis
          </h4>
          <p className="text-xs sm:text-sm font-medium text-slate-600 leading-relaxed">
            No waiting days for an expert visit. Get immediate feedback right in the field using your phone camera.
          </p>
        </div>

        <div className="neo-card p-6">
          <div className="w-12 h-12 rounded-xl neo-border-sm bg-amber-200 flex items-center justify-center mb-3 neo-shadow-sm">
            <Leaf className="w-6 h-6 text-slate-800" />
          </div>
          <h4 className="font-extrabold text-lg text-slate-900 mb-1">
            Organic-First Solutions
          </h4>
          <p className="text-xs sm:text-sm font-medium text-slate-600 leading-relaxed">
            We prioritize preventive neem solutions, cultural farming techniques, and natural predators before recommending chemical treatments.
          </p>
        </div>

        <div className="neo-card p-6">
          <div className="w-12 h-12 rounded-xl neo-border-sm bg-indigo-200 flex items-center justify-center mb-3 neo-shadow-sm">
            <IndianRupee className="w-6 h-6 text-slate-800" />
          </div>
          <h4 className="font-extrabold text-lg text-slate-900 mb-1">
            Save on Input Costs
          </h4>
          <p className="text-xs sm:text-sm font-medium text-slate-600 leading-relaxed">
            Accurate identification prevents misdiagnosis and stops the wasteful application of ineffective pesticides.
          </p>
        </div>

        <div className="neo-card p-6">
          <div className="w-12 h-12 rounded-xl neo-border-sm bg-sky-200 flex items-center justify-center mb-3 neo-shadow-sm">
            <Shield className="w-6 h-6 text-slate-800" />
          </div>
          <h4 className="font-extrabold text-lg text-slate-900 mb-1">
            100% Private & No Accounts Needed
          </h4>
          <p className="text-xs sm:text-sm font-medium text-slate-600 leading-relaxed">
            No sign-up forms, passwords, or data tracking. Your photos remain in your browser session and are never sold or stored permanently in cloud databases.
          </p>
        </div>
      </div>

      {/* Advisory Notice */}
      <div className="neo-card p-6 bg-emerald-50/50 neo-shadow">
        <div className="flex items-center gap-3 mb-2">
          <Info className="w-5 h-5 text-emerald-700" />
          <h4 className="font-extrabold text-slate-900 text-base">
            Agricultural Extension Notice
          </h4>
        </div>
        <p className="text-xs sm:text-sm font-medium text-slate-700 leading-relaxed">
          FasalMitra AI is an educational and diagnostic companion designed to assist field observation. Pesticide regulations and registrations vary across states and districts. Before applying commercial chemical treatments, always check product labels and consult with your local Block Agriculture Officer or Krishi Vigyan Kendra (KVK).
        </p>
      </div>

    </section>
  );
}
