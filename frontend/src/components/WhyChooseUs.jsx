import React from 'react';
import { Zap, Leaf, ShieldCheck, HeartHandshake } from 'lucide-react';

export default function WhyChooseUs() {
  const features = [
    {
      title: 'Instant Field Diagnosis',
      badge: '⚡ 5-Second Scan',
      desc: 'Point your smartphone camera directly at any leaf or pest in your field. Get instant pest identification without waiting days for lab tests.',
      icon: <Zap className="w-6 h-6 text-slate-800" />,
      iconBg: 'bg-rose-200',
    },
    {
      title: 'Organic-First Remedies',
      badge: '🌿 Eco-Friendly',
      desc: 'Access verified neem spray solutions, yellow sticky traps, and biological predators to safeguard crop yield while protecting soil health.',
      icon: <Leaf className="w-6 h-6 text-slate-800" />,
      iconBg: 'bg-sky-200',
    },
    {
      title: '102 Pest Species',
      badge: '🎯 High Accuracy',
      desc: 'Powered by deep computer vision trained on benchmark agricultural datasets covering rice, cotton, wheat, maize, and vegetables.',
      icon: <ShieldCheck className="w-6 h-6 text-slate-800" />,
      iconBg: 'bg-indigo-200',
    },
    {
      title: '100% Free for Farmers',
      badge: '💰 Save Input Costs',
      desc: 'Completely free with zero registration and zero cloud storage. Prevent misdiagnosis so you only spend money on treatments that work.',
      icon: <HeartHandshake className="w-6 h-6 text-slate-800" />,
      iconBg: 'bg-emerald-200',
    },
  ];

  return (
    <section className="max-w-6xl mx-auto px-4 py-12">
      {/* Header */}
      <div className="text-center mb-10">
        <div className="inline-block bg-rose-200 text-slate-800 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          Why Farmers Choose FasalMitra
        </div>
        <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 mb-2">
          Everything You Need to Protect Your Crop
        </h2>
        <p className="text-sm sm:text-base font-medium text-slate-600 max-w-lg mx-auto">
          Built specifically for Indian farmers to recognize early crop damage and save harvest yield.
        </p>
      </div>

      {/* 4 Feature Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {features.map((item, idx) => (
          <div key={idx} className="neo-card p-6 text-center flex flex-col items-center">
            {/* Squircle Icon Box */}
            <div className={`w-14 h-14 rounded-2xl neo-border-sm ${item.iconBg} flex items-center justify-center neo-shadow-sm mb-4`}>
              {item.icon}
            </div>

            <h3 className="font-extrabold text-slate-900 text-lg mb-1">
              {item.title}
            </h3>
            
            <p className="text-xs font-extrabold text-emerald-700 mb-3 bg-emerald-50 px-2.5 py-0.5 rounded-full neo-border-sm">
              {item.badge}
            </p>

            <p className="text-xs font-medium text-slate-600 leading-relaxed">
              {item.desc}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
