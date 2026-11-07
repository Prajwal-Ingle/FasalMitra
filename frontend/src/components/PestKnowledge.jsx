import React, { useState, useEffect } from 'react';
import { Search, Bug, Filter } from 'lucide-react';

export default function PestKnowledge({ onSelectPest }) {
  const [pests, setPests] = useState([]);
  const [query, setQuery] = useState('');
  const [selectedCrop, setSelectedCrop] = useState('All Crops');
  const [loading, setLoading] = useState(true);

  const crops = ['All Crops', 'Rice', 'Wheat', 'Cotton', 'Maize', 'Tomato', 'Soybean', 'Mango', 'Citrus'];

  useEffect(() => {
    setLoading(true);
    let url = '/api/pests?';
    if (query) url += `query=${encodeURIComponent(query)}&`;
    if (selectedCrop !== 'All Crops') url += `crop=${encodeURIComponent(selectedCrop)}`;

    fetch(url)
      .then(res => res.json())
      .then(data => {
        setPests(data.pests || []);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching pests:', err);
        setLoading(false);
      });
  }, [query, selectedCrop]);

  return (
    <section className="max-w-6xl mx-auto px-4 py-8">
      
      {/* Header */}
      <div className="mb-8">
        <div className="inline-flex items-center gap-2 bg-sky-200 text-slate-900 font-extrabold text-xs px-4 py-1.5 rounded-full neo-border-sm neo-shadow-sm mb-3">
          <span>📚 Agronomic Reference Library</span>
        </div>
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-slate-900 mb-2">
          Pest Knowledge Centre
        </h1>
        <p className="text-sm sm:text-base font-medium text-slate-600">
          Learn how to recognize common crop pests in the field, spot early damage symptoms, and protect your crops naturally.
        </p>
      </div>

      {/* Filter and Search Bar */}
      <div className="neo-card p-6 mb-8">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
          
          {/* Search Input */}
          <div className="md:col-span-7 relative">
            <Search className="w-5 h-5 text-slate-400 absolute left-4 top-3.5" />
            <input
              type="text"
              placeholder="Search by pest name or symptom (e.g. aphid, borer, fly, hopper)..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full neo-border-sm rounded-xl pl-12 pr-4 py-2.5 text-sm font-bold bg-white text-slate-800 neo-shadow-sm focus:outline-none"
            />
          </div>

          {/* Crop Dropdown */}
          <div className="md:col-span-5 flex items-center gap-2">
            <Filter className="w-4 h-4 text-slate-500 shrink-0" />
            <select
              value={selectedCrop}
              onChange={(e) => setSelectedCrop(e.target.value)}
              className="w-full neo-border-sm rounded-xl px-4 py-2.5 text-sm font-bold bg-white text-slate-800 neo-shadow-sm focus:outline-none"
            >
              {crops.map((c, i) => (
                <option key={i} value={c}>{c}</option>
              ))}
            </select>
          </div>

        </div>

        {/* Quick Crop Filter Chips */}
        <div className="flex flex-wrap gap-2 mt-4 pt-4 border-t-2 border-slate-100">
          {crops.map((c, i) => (
            <button
              key={i}
              onClick={() => setSelectedCrop(c)}
              className={`text-xs font-extrabold px-3 py-1.5 rounded-full neo-border-sm transition-all cursor-pointer ${
                selectedCrop === c
                  ? 'bg-emerald-300 text-slate-900 neo-shadow-sm -translate-y-0.5'
                  : 'bg-white text-slate-600 hover:bg-slate-50'
              }`}
            >
              {c}
            </button>
          ))}
        </div>
      </div>

      {/* Pests Grid */}
      {loading ? (
        <div className="text-center py-16 font-extrabold text-slate-500">
          Loading verified pest encyclopedia...
        </div>
      ) : pests.length === 0 ? (
        <div className="neo-card p-12 text-center">
          <Bug className="w-12 h-12 text-slate-400 mx-auto mb-3" />
          <h3 className="text-xl font-extrabold text-slate-800 mb-1">No Pests Found</h3>
          <p className="text-xs font-medium text-slate-500">Try searching for 'aphid', 'hopper', 'borer', or 'caterpillar'.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {pests.map((p, idx) => (
            <div key={idx} className="neo-card p-6 flex flex-col justify-between">
              <div>
                {/* Header */}
                <div className="flex items-start justify-between gap-3 mb-3">
                  <div className="flex items-center gap-3">
                    <div className="w-11 h-11 rounded-xl neo-border-sm bg-rose-200 flex items-center justify-center text-xl neo-shadow-sm">
                      🐛
                    </div>
                    <div>
                      <h3 className="text-lg font-extrabold text-slate-900 leading-tight">
                        {p.common_name}
                      </h3>
                      {p.hindi_name && (
                        <p className="text-xs font-bold text-emerald-700">({p.hindi_name})</p>
                      )}
                    </div>
                  </div>
                  <span className="text-[11px] font-extrabold px-2.5 py-1 rounded-full neo-border-sm bg-slate-100 text-slate-700">
                    {p.crops.join(', ')}
                  </span>
                </div>

                <p className="text-xs font-bold text-slate-400 italic mb-3">
                  {p.scientific_name}
                </p>

                {/* Symptoms */}
                <div className="bg-slate-50 neo-border-sm rounded-xl p-3 mb-3">
                  <span className="text-xs font-extrabold text-slate-800 block mb-0.5">How to Spot on Plant:</span>
                  <p className="text-xs font-medium text-slate-600 leading-relaxed">{p.how_to_spot}</p>
                </div>

                {/* Organic & Chemical */}
                <div className="space-y-2 mb-4">
                  <div className="bg-emerald-50/70 neo-border-sm rounded-xl p-2.5">
                    <span className="text-xs font-extrabold text-emerald-800 block">🌿 Organic Care:</span>
                    <p className="text-xs font-medium text-slate-700 whitespace-pre-line leading-relaxed">{p.prevention_organic}</p>
                  </div>
                  <div className="bg-sky-50/70 neo-border-sm rounded-xl p-2.5">
                    <span className="text-xs font-extrabold text-sky-800 block">🧪 Field Spray:</span>
                    <p className="text-xs font-medium text-slate-700 leading-relaxed">{p.recommended_treatment}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

    </section>
  );
}
