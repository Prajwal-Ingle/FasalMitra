import React from 'react';
import { Star } from 'lucide-react';

export default function FarmerStories() {
  const reviews = [
    {
      stars: 5,
      quote: '"FasalMitra spotted Rice Leaf Folder caterpillars on my paddy crop almost two weeks before major yellowing occurred. The neem spray recommendation completely protected our 25-acre harvest!"',
      name: 'Gurpreet Singh',
      crop: 'Paddy & Wheat Grower',
      location: 'Ludhiana, Punjab',
      avatar: '🌾',
      avatarBg: 'bg-rose-200',
    },
    {
      stars: 5,
      quote: '"Whiteflies and aphids used to destroy our cotton crop every monsoon. Now I just scan suspect leaves directly from my mobile browser right in the field. Instant diagnosis and 100% free."',
      name: 'Ramesh Patel',
      crop: 'Cotton & Groundnut Grower',
      location: 'Rajkot, Gujarat',
      avatar: '🌱',
      avatarBg: 'bg-sky-200',
    },
    {
      stars: 5,
      quote: '"We saved over ₹8,000 on unnecessary chemical pesticides because FasalMitra confirmed that the insects on our soybean were beneficial ladybird beetles and not destructive pests."',
      name: 'Balasaheb Shinde',
      crop: 'Soybean & Sugarcane Farmer',
      location: 'Nashik, Maharashtra',
      avatar: '🚜',
      avatarBg: 'bg-emerald-200',
    },
  ];

  return (
    <section className="max-w-6xl mx-auto px-4 py-12">
      {/* Header */}
      <div className="text-center mb-10">
        <div className="inline-block bg-emerald-200 text-slate-800 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          Farmer Testimonials
        </div>
        <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 mb-2">
          What Indian Farmers Say
        </h2>
        <p className="text-sm sm:text-base font-medium text-slate-600 max-w-lg mx-auto">
          Real growers protecting their harvest and lowering pesticide expenses with FasalMitra AI.
        </p>
      </div>

      {/* 3 Review Cards matching Image 4 style */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {reviews.map((rev, idx) => (
          <div key={idx} className="neo-card p-6 flex flex-col justify-between">
            <div>
              {/* 5 Stars */}
              <div className="flex items-center gap-1 mb-4">
                {[...Array(rev.stars)].map((_, i) => (
                  <Star key={i} className="w-4 h-4 fill-amber-400 text-amber-400" />
                ))}
              </div>

              {/* Quote */}
              <p className="text-xs sm:text-sm font-medium text-slate-700 leading-relaxed mb-6 italic">
                {rev.quote}
              </p>
            </div>

            {/* Author Footer */}
            <div className="flex items-center gap-3 pt-4 border-t-2 border-slate-100">
              <div className={`w-11 h-11 rounded-xl neo-border-sm ${rev.avatarBg} flex items-center justify-center font-extrabold text-slate-800 text-xl neo-shadow-sm`}>
                {rev.avatar}
              </div>
              <div>
                <h4 className="font-extrabold text-slate-900 text-sm leading-tight">
                  {rev.name}
                </h4>
                <p className="text-xs font-bold text-emerald-700">
                  {rev.crop}
                </p>
                <p className="text-[11px] font-medium text-slate-500">
                  {rev.location}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
