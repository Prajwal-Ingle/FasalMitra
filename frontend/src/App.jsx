import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import PopularPests from './components/PopularPests';
import WhyChooseUs from './components/WhyChooseUs';
import FarmerStories from './components/FarmerStories';
import FooterCTA from './components/FooterCTA';
import PestDetector from './components/PestDetector';
import PestKnowledge from './components/PestKnowledge';
import MyDetections from './components/MyDetections';
import AboutSection from './components/AboutSection';

export default function App() {
  const [activePage, setActivePage] = useState('home');
  const [history, setHistory] = useState([]);
  const [selectedSamplePreset, setSelectedSamplePreset] = useState(null);

  // Load history from session storage on mount
  useEffect(() => {
    try {
      const saved = sessionStorage.getItem('fasalmitra_history');
      if (saved) {
        setHistory(JSON.parse(saved));
      }
    } catch (e) {
      console.warn('Could not read session history', e);
    }
  }, []);

  // Save history to session storage
  const handleAddDetection = (record) => {
    const updated = [record, ...history];
    setHistory(updated);
    try {
      sessionStorage.setItem('fasalmitra_history', JSON.stringify(updated));
    } catch (e) {
      console.warn('Could not save session history', e);
    }
  };

  const handleClearHistory = () => {
    setHistory([]);
    try {
      sessionStorage.removeItem('fasalmitra_history');
    } catch (e) {
      console.warn('Could not clear session history', e);
    }
  };

  const handleSampleClickFromHome = () => {
    setSelectedSamplePreset('sample_pest_1.jpg');
    setActivePage('detect');
  };

  return (
    <div className="min-h-screen bg-[#FFFDF7] text-slate-800 flex flex-col justify-between selection:bg-emerald-200">
      
      {/* Top Floating Neo-Brutalist Navbar */}
      <Navbar activePage={activePage} setActivePage={setActivePage} />

      {/* Main Content Viewport */}
      <main className="flex-grow">
        {activePage === 'home' && (
          <div>
            <Hero
              onStartDetection={() => setActivePage('detect')}
              onExplorePests={() => setActivePage('knowledge')}
              onSampleClick={handleSampleClickFromHome}
            />
            <PopularPests onSelectPest={() => setActivePage('knowledge')} />
            <WhyChooseUs />
            <FarmerStories />
            <FooterCTA
              onStartDetection={() => setActivePage('detect')}
              onExploreKnowledge={() => setActivePage('knowledge')}
            />
          </div>
        )}

        {activePage === 'detect' && (
          <PestDetector
            onDetectionComplete={handleAddDetection}
            initialSample={selectedSamplePreset}
          />
        )}

        {activePage === 'knowledge' && (
          <PestKnowledge onSelectPest={() => setActivePage('detect')} />
        )}

        {activePage === 'history' && (
          <MyDetections
            history={history}
            onClearHistory={handleClearHistory}
            onStartDetection={() => setActivePage('detect')}
          />
        )}

        {activePage === 'about' && (
          <AboutSection />
        )}
      </main>

      {/* Footer */}
      <footer className="border-t-[2.5px] border-slate-800 bg-white py-8 px-4 text-center mt-16">
        <div className="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-lg neo-border-sm bg-pink-100 flex items-center justify-center text-sm neo-shadow-sm">
              🌾
            </div>
            <span className="font-extrabold text-slate-900 text-sm">FasalMitra AI (फसल मित्र)</span>
          </div>
          <p className="text-xs font-bold text-slate-500">
            Smart Crop Protection &bull; Zero Cloud Storage &bull; Free for All Farmers
          </p>
          <div className="text-xs font-extrabold text-emerald-600">
            Powered by Verified Vision AI
          </div>
        </div>
      </footer>

    </div>
  );
}
