import React from 'react';
import { useTranslation } from '../useTranslation';

export default function Footer() {
  const { t } = useTranslation();

  return (
    <footer className="footer">
      <p>{t('footer')}</p>
    </footer>
  );
}
