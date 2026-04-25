import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useTranslation } from '../useTranslation';

export default function Home() {
  const navigate = useNavigate();
  const { t, language } = useTranslation();

  console.log('Home component rendered with language:', language);
  console.log('homeTitle translation:', t('homeTitle'));

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1>{t('homeTitle')}</h1>
          <p>{t('homeDesc')}</p>
          <div className="hero-actions">
            <button className="btn btn-primary" onClick={() => navigate('/capture')}>
              🔍 {t('startBtn')}
            </button>
          </div>
        </div>
        <div className="hero-visual">
          <div className="hero-icon">🌾</div>
        </div>
      </section>

      <section className="details">
        <div className="detail-card">
          <h3>{t('card1Title')}</h3>
          <p>{t('card1Desc')}</p>
        </div>
        <div className="detail-card">
          <h3>{t('card2Title')}</h3>
          <p>{t('card2Desc')}</p>
        </div>
        <div className="detail-card">
          <h3>{t('card3Title')}</h3>
          <p>{t('card3Desc')}</p>
        </div>
        <div className="detail-card">
          <h3>{t('card4Title')}</h3>
          <p>{t('card4Desc')}</p>
        </div>
        <div className="detail-card">
          <h3>{t('card5Title')}</h3>
          <p>{t('card5Desc')}</p>
        </div>
        <div className="detail-card">
          <h3>{t('card6Title')}</h3>
          <p>{t('card6Desc')}</p>
        </div>
      </section>
    </div>
  );
}
