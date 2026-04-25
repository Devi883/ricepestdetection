import { useContext } from 'react';
import { LanguageContext } from './LanguageContext';
import { translations } from './i18n';

export function useTranslation() {
  const { language } = useContext(LanguageContext);
  
  return {
    t: (key) => translations[language]?.[key] || translations['en'][key],
    language
  };
}
