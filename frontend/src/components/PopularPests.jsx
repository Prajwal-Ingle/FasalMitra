import React from 'react';
import { Star, ShieldAlert, Bug, Leaf } from 'lucide-react';

export default function PopularPests({ onSelectPest }) {
  const threats = [
    {
      id: 'rice-leaf-roller',
      title: 'Rice Leaf Roller (Folder)',
      hindi: 'धान का पत्ता लपेटक कीट',
      scientific: 'Cnaphalocrocis medinalis',
      crop: 'Rice (Paddy)',
      rating: '★ High Threat',
      symptoms: 'Caterpillars fold leaf blades longitudinally into tubes, scraping green tissue inside and leaving papery white streaks.',
      organic: 'Neem spray (1500 ppm @ 3ml/L) & Trichogramma cards',
      icon: '🌾',
      iconBg: 'bg-rose-200',
    },
    {
      id: 'brown-plant-hopper',
      title: 'Brown Planthopper (BPH)',
      hindi: 'भूरा फुदका कीट (माहू)',
      scientific: 'Nilaparvata lugens',
      crop: 'Rice',
      rating: '★ Critical Threat',
      symptoms: 'Hoppers cluster at stem bases, draining sap. Plants dry out rapidly in circular scorched patches called "Hopperburn".',
      organic: 'Alleyway aeration (30cm every 2m) & alternate wetting/drying',
      icon: '🐛',
      iconBg: 'bg-sky-200',
    },
    {
      id: 'cotton-aphids',
      title: 'Cotton Aphids & Whitefly',
      hindi: 'कपास का चेपा व सफेद मक्खी',
      scientific: 'Aphis gossypii & Whiteflies',
      crop: 'Cotton, Tomato',
      rating: '★ High Threat',
      symptoms: 'Dense sap-sucking colonies under leaves. Foliage curls downward, excreting sticky honeydew that forms dark sooty mold.',
      organic: 'Yellow sticky cards (15/acre) & fermented buttermilk spray',
      icon: '☁️',
      iconBg: 'bg-indigo-200',
    },
    {
      id: 'armyworm',
      title: 'Fall Armyworm (FAW)',
      hindi: 'मक्के का सैनिक कीट',
      scientific: 'Spodoptera frugiperda',
      crop: 'Maize, Wheat',
      rating: '★ Severe Threat',
      symptoms: 'Aggressive grazing inside central whorls leaving skeletonized leaves and copious sawdust-like frass pellets.',
      organic: 'Wood ash/sand in whorl cups & bio-agent Bt kurstaki dust',
      icon: '🌽',
      iconBg: 'bg-emerald-200',
    },
  ];

  return (
    <section className="max-w-6xl mx-auto px-4 py-12">
      {/* Section Header */}
      <div className="text-center mb-10">
        <div className="inline-block bg-sky-200 text-slate-800 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          Major Agricultural Threats
        </div>
        <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 mb-2">
          Explore Common Crop Pests
        </h2>
        <p className="text-sm sm:text-base font-medium text-slate-600 max-w-lg mx-auto">
          Recognize early leaf damage symptoms on your crops and prevent yield losses with verified remedies.
        </p>
      </div>

      {/* 2x2 Grid matching Image 2 style */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {threats.map((t) => (
          <div
            key={t.id}
            onClick={() => onSelectPest && onSelectPest(t.id)}
            className="neo-card p-6 cursor-pointer group flex flex-col justify-between"
          >
            <div>
              <div className="flex items-start justify-between gap-4 mb-4">
                {/* Icon badge */}
                <div className={`w-12 h-12 rounded-2xl neo-border-sm ${t.iconBg} flex items-center justify-center font-extrabold text-2xl neo-shadow-sm group-hover:scale-105 transition-transform`}>
                  {t.icon}
                </div>

                {/* Threat level pill */}
                <div className="flex items-center gap-1.5 bg-rose-50 text-rose-700 neo-border-sm px-3 py-1 rounded-full neo-shadow-sm text-xs font-extrabold">
                  <ShieldAlert className="w-3.5 h-3.5 text-rose-600" />
                  <span>{t.rating}</span>
                </div>
              </div>

              {/* Title & Hindi */}
              <h3 className="font-extrabold text-slate-900 text-xl mb-0.5 group-hover:text-emerald-600 transition-colors">
                {t.title}
              </h3>
              <p className="text-xs font-bold text-emerald-700 mb-1">
                {t.hindi} &bull; <span className="italic font-medium text-slate-400">{t.scientific}</span>
              </p>

              {/* Symptoms */}
              <p className="text-xs font-medium text-slate-600 mb-4 leading-relaxed">
                {t.symptoms}
              </p>
            </div>

            {/* Organic Remedy Footer */}
            <div className="pt-3 border-t-2 border-slate-100 flex items-center justify-between text-xs font-bold text-slate-600">
              <span className="flex items-center gap-1.5 text-emerald-800">
                <Leaf className="w-4 h-4 text-emerald-600" />
                {t.organic}
              </span>
              <span className="bg-slate-100 text-slate-700 px-2 py-0.5 rounded-md neo-border-sm text-[11px]">
                {t.crop}
              </span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
