import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import TaskManager from './pages/TaskManager';
import Workflows from './pages/Workflows';
import Analytics from './pages/Analytics';
import Settings from './pages/Settings';
import Navbar from './components/Navbar';
import Notifications from './components/Notifications';
import './styles/globals.css';

const App = () => {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [theme, setTheme] = useState('dark');
  const [notifications, setNotifications] = useState([]);

  const toggleSidebar = () => setSidebarOpen(!sidebarOpen);
  const toggleTheme = () => setTheme(theme === 'dark' ? 'light' : 'dark');

  const addNotification = (message, type = 'info') => {
    const id = Date.now();
    setNotifications(prev => [...prev, { id, message, type }]);
    setTimeout(() => {
      setNotifications(prev => prev.filter(n => n.id !== id));
    }, 3000);
  };

  return (
    <Router>
      <div className={`app-container ${theme}`}>
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="app-layout">
          <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
          <main className={`main-content ${sidebarOpen ? 'expanded' : 'collapsed'}`}>
            <Navbar 
              toggleTheme={toggleTheme} 
              theme={theme} 
              toggleSidebar={toggleSidebar}
            />
            <AnimatePresence mode="wait">
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/tasks" element={<TaskManager />} />
                <Route path="/workflows" element={<Workflows />} />
                <Route path="/analytics" element={<Analytics />} />
                <Route path="/settings" element={<Settings />} />
              </Routes>
            </AnimatePresence>
          </main>
          <Notifications notifications={notifications} />
        </motion.div>
      </div>
    </Router>
  );
};

export default App;
