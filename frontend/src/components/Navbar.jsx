import React, { useState } from 'react';
import { Menu, X, Camera, ShieldCheck } from 'lucide-react';

export default function Navbar({ activePage, setActivePage }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navItems = [
    { id: 'home', label: 'Home' },
    { id: 'detect', label: 'Pest Detection' },
    { id: 'knowledge', label: 'Pest Knowledge' },
    { id: 'history', label: 'My Detections' },
    { id: 'about', label: 'About' },
  ];

  return (
    <header className="sticky top-4 z-50 px-4 mb-6">
      <div className="max-w-6xl mx-auto bg-white neo-border rounded-full neo-shadow px-4 md:px-6 py-2.5 flex items-center justify-between">
        
        {/* Brand Logo */}
        <div 
          onClick={() => setActivePage('home')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl neo-border-sm bg-pink-100 flex items-center justify-center text-xl neo-shadow-sm group-hover:scale-105 transition-transform">
            🌾
          </div>
          <div>
            <div className="flex items-baseline gap-1.5">
              <span className="font-extrabold text-xl tracking-tight text-slate-800">FasalMitra</span>
              <span className="text-sm font-bold text-emerald-600 hidden sm:inline">(फसल मित्र)</span>
            </div>
            <p className="text-[11px] font-semibold text-slate-500 hidden md:block -mt-1">Smart Crop Protection</p>
          </div>
        </div>

        {/* Desktop Navigation Links */}
        <nav className="hidden md:flex items-center gap-1 lg:gap-2">
          {navItems.map((item) => {
            const isActive = activePage === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActivePage(item.id)}
                className={`px-3.5 py-1.5 rounded-full font-bold text-sm transition-all cursor-pointer ${
                  isActive
                    ? 'bg-emerald-100 text-emerald-800 neo-border-sm neo-shadow-sm -translate-y-0.5'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
                }`}
              >
                {item.label}
              </button>
            );
          })}
        </nav>

        {/* Right CTA / Ready Badge */}
        <div className="hidden sm:flex items-center gap-3">
          <div className="hidden lg:flex items-center gap-2 bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full text-xs font-bold neo-border-sm neo-shadow-sm">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            Diagnosis Ready
          </div>
          <button
            onClick={() => setActivePage('detect')}
            className="flex items-center gap-2 bg-emerald-500 hover:bg-emerald-600 text-white font-extrabold text-sm px-4 py-2 rounded-full neo-btn cursor-pointer"
          >
            <Camera className="w-4 h-4" />
            <span>Scan Crop Leaf</span>
          </button>
        </div>

        {/* Mobile Hamburger Toggle */}
        <div className="flex sm:hidden">
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="p-1.5 rounded-lg neo-border-sm bg-slate-50 text-slate-800"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>

      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="sm:hidden mt-2 bg-white neo-border rounded-2xl neo-shadow p-4 flex flex-col gap-2">
          {navItems.map((item) => (
            <button
              key={item.id}
              onClick={() => {
                setActivePage(item.id);
                setMobileMenuOpen(false);
              }}
              className={`text-left px-4 py-2.5 rounded-xl font-bold text-sm ${
                activePage === item.id
                  ? 'bg-emerald-100 text-emerald-800 neo-border-sm'
                  : 'text-slate-700 hover:bg-slate-50'
              }`}
            >
              {item.label}
            </button>
          ))}
          <button
            onClick={() => {
              setActivePage('detect');
              setMobileMenuOpen(false);
            }}
            className="mt-2 w-full flex items-center justify-center gap-2 bg-emerald-500 text-white font-extrabold py-2.5 rounded-xl neo-btn"
          >
            <Camera className="w-4 h-4" />
            <span>Scan Crop Leaf Now</span>
          </button>
        </div>
      )}
    </header>
  );
}
