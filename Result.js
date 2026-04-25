import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useTranslation } from '../useTranslation';

export default function Result() {
  const navigate = useNavigate();
  const location = useLocation();
  const { t, language } = useTranslation();
  
  const state = location.state?.result || {
    index: 0,
    name: t('unknownPest'),
    telugu_name: t('unknownPest'),
    info: {
      impact: t('unableToDetect'),
      eggs: t('noEggInfo'),
      control: t('noControlInfo')
    }
  };
  
  const imageData = location.state?.imageData;
  
  // Debug logging
  console.log('Result page loaded');
  console.log('Language from context:', language);
  console.log('Result data:', state);
  console.log('English name:', state.name);
  console.log('Telugu name:', state.telugu_name);
  console.log('Info object:', state.info);
  console.log('Impact value:', state.info?.impact);

  return (
    <div className="result">
      <h2 style={{ marginBottom: '2rem', fontSize: '2rem' }}>{t('resultTitle')}</h2>
      
      <div className="result-container">
        {/* Left: Image and Status */}
        <div className="result-image-section">
          <div className="result-image" style={{ background: 'linear-gradient(135deg, rgba(16,185,129,0.1), rgba(124,58,237,0.1))' }}>
            {imageData ? (
              <img 
                src={imageData} 
                alt="Captured pest" 
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  borderRadius: '12px'
                }}
              />
            ) : (
              <div style={{ 
                width: '100%', 
                height: '100%', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center',
                fontSize: '4rem'
              }}>
                🌾
              </div>
            )}
          </div>
          
          <div className="result-status">
            <div className="pest-name">{state.name}<br /><span style={{ fontSize: '0.9rem', color: 'var(--secondary)', marginTop: '0.5rem' }}>{state.telugu_name}</span></div>
          </div>
        </div>

        {/* Right: Details */}
        <div className="result-details">
          <div className="detail-section">
            <h3>{t('impact')}</h3>
            <p>{state.info?.impact || t('unableToDetect')}</p>
          </div>

          <div className="detail-section">
            <h3>{t('eggs')}</h3>
            <p>{state.info?.eggs || t('noEggInfo')}</p>
          </div>

          <div className="detail-section">
            <h3>{t('control')}</h3>
            <p>{state.info?.control || t('noControlInfo')}</p>
          </div>

          <div className="detail-section">
            <h3>{t('pesticide')}</h3>
            <p>{state.info?.pesticide || t('noPesticideInfo')}</p>
          </div>

          <div className="action-buttons">
            <button className="btn btn-primary" onClick={() => navigate('/capture')}>
              {t('scanAgain')}
            </button>
            <button className="btn btn-secondary" onClick={() => navigate('/')}>
              {t('goHome')}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
