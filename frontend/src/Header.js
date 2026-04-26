import React, { useContext } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { LanguageContext } from '../LanguageContext';

export default function Header() {
  const { language, setLanguage } = useContext(LanguageContext);
  const location = useLocation();
  const isHomePage = location.pathname === '/';

  const handleLanguageToggle = () => {
    console.log('Language toggle clicked. Current language:', language);
    const newLanguage = language === 'en' ? 'te' : 'en';
    console.log('Setting new language to:', newLanguage);
    setLanguage(newLanguage);
  };

  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          🌾 Rice Pest Detector
        </Link>
        <nav className="nav-links">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/capture" className="nav-link">Scan</Link>
          {isHomePage && (
            <button 
              className="nav-link language-toggle"
              onClick={handleLanguageToggle}
              style={{
                background: 'rgba(16, 185, 129, 0.2)',
                border: '1px solid var(--primary)',
                cursor: 'pointer',
                fontSize: '0.95rem',
                fontWeight: '500',
                color: 'var(--primary)',
                padding: '0.5rem 1rem',
                borderRadius: '0.5rem',
                transition: 'all 0.3s ease'
              }}
            >
              {language === 'en' ? '🇮🇳 తెలుగు' : '🇬🇧 English'}
            </button>
          )}
        </nav>
      </div>
    </header>
  );
}
