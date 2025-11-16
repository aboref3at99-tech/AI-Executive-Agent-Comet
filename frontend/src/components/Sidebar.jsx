import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FiHome, FiCheckSquare, FiGitBranch, FiBarChart2, FiSettings, FiChevronDown, FiMenu, FiX, FiLogOut, FiUser } from 'react-icons/fi';
import { motion, AnimatePresence } from 'framer-motion';

const Sidebar = ({ isOpen, setIsOpen, onLogout }) => {
  const location = useLocation();
  const [expandedMenu, setExpandedMenu] = useState(null);

  const menuItems = [
    { label: 'Dashboard', icon: FiHome, path: '/', submenu: [] },
    { label: 'Tasks', icon: FiCheckSquare, path: '/tasks', submenu: [] },
    { label: 'Workflows', icon: FiGitBranch, path: '/workflows', submenu: [] },
    { label: 'Analytics', icon: FiBarChart2, path: '/analytics', submenu: [] },
    { label: 'Settings', icon: FiSettings, path: '/settings', submenu: [] },
  ];

  const isActive = (path) => location.pathname === path;

  const toggleSubmenu = (label) => {
    setExpandedMenu(expandedMenu === label ? null : label);
  };

  const sidebarVariants = {
    open: { x: 0, opacity: 1 },
    closed: { x: '-100%', opacity: 0 },
  };

  return (
    <>
      {/* Mobile Menu Toggle */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="fixed md:hidden top-4 left-4 z-50 p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
      >
        {isOpen ? <FiX size={24} /> : <FiMenu size={24} />}
      </button>

      {/* Sidebar Overlay (Mobile) */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 md:hidden z-40"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Sidebar */}
      <motion.aside
        variants={sidebarVariants}
        initial={false}
        animate={isOpen ? 'open' : 'closed'}
        transition={{ duration: 0.3 }}
        className="fixed left-0 top-0 h-screen w-64 bg-gradient-to-b from-gray-900 to-gray-800 text-white shadow-xl md:relative md:translate-x-0 z-40"
      >
        {/* Header */}
        <div className="p-6 border-b border-gray-700">
          <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
            Comet
          </h1>
          <p className="text-gray-400 text-sm mt-1">Executive Agent</p>
        </div>

        {/* Navigation Menu */}
        <nav className="flex-1 overflow-y-auto py-4">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isItemActive = isActive(item.path);

            return (
              <div key={item.label}>
                <Link
                  to={item.path}
                  onClick={() => {
                    if (item.submenu.length > 0) {
                      toggleSubmenu(item.label);
                    } else {
                      setIsOpen(false);
                    }
                  }}
                  className={`flex items-center justify-between px-6 py-3 mx-2 rounded-lg transition-all duration-200 group ${
                    isItemActive
                      ? 'bg-blue-600 text-white shadow-lg'
                      : 'text-gray-300 hover:bg-gray-700'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <Icon size={20} />
                    <span className="font-medium">{item.label}</span>
                  </div>
                  {item.submenu.length > 0 && (
                    <FiChevronDown
                      size={18}
                      className={`transition-transform ${
                        expandedMenu === item.label ? 'rotate-180' : ''
                      }`}
                    />
                  )}
                </Link>

                {/* Submenu */}
                <AnimatePresence>
                  {expandedMenu === item.label && item.submenu.length > 0 && (
                    <motion.div
                      initial={{ height: 0, opacity: 0 }}
                      animate={{ height: 'auto', opacity: 1 }}
                      exit={{ height: 0, opacity: 0 }}
                      transition={{ duration: 0.2 }}
                      className="overflow-hidden"
                    >
                      {item.submenu.map((subitem) => (
                        <Link
                          key={subitem.path}
                          to={subitem.path}
                          className="block px-6 py-2 ml-8 text-gray-300 hover:text-white hover:bg-gray-700 rounded-lg transition-all"
                        >
                          {subitem.label}
                        </Link>
                      ))}
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            );
          })}
        </nav>

        {/* User Section */}
        <div className="border-t border-gray-700 p-4">
          <div className="flex items-center gap-3 px-2 py-3 rounded-lg hover:bg-gray-700 transition-all cursor-pointer mb-3">
            <div className="w-10 h-10 rounded-full bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center">
              <FiUser size={20} />
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium truncate">Admin User</p>
              <p className="text-xs text-gray-400 truncate">agent@comet.ai</p>
            </div>
          </div>

          <button
            onClick={onLogout}
            className="w-full flex items-center gap-3 px-4 py-2 rounded-lg text-gray-300 hover:bg-red-600 hover:text-white transition-all duration-200"
          >
            <FiLogOut size={18} />
            <span>Logout</span>
          </button>
        </div>
      </motion.aside>
    </>
  );
};

export default Sidebar;
