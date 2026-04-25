import React, { createContext, useState, useEffect } from 'react';

export const LanguageContext = createContext();

export function LanguageProvider({ children }) {
  const [language, setLanguage] = useState(() => {
    // Get language from localStorage on init
    const savedLanguage = localStorage.getItem('language') || 'en';
    console.log('LanguageProvider initialized with language:', savedLanguage);
    return savedLanguage;
  });
  
  // Save language to localStorage whenever it changes
  useEffect(() => {
    console.log('Language changed to:', language);
    localStorage.setItem('language', language);
  }, [language]);
  
  return (
    <LanguageContext.Provider value={{ language, setLanguage }}>
      {children}
    </LanguageContext.Provider>
  );
}
