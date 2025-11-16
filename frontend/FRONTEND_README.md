# Comet AI Executive Agent - React Frontend

## 📋 Overview

The Comet Control Panel is an advanced, professional web interface for managing the AI Executive Agent system. Built with React 18 and modern web technologies, it provides a comprehensive dashboard for monitoring, controlling, and automating intelligent workflows.

### Key Features

- **Real-time Dashboard**: Live metrics and system status monitoring
- **Task Management**: Create, execute, and track autonomous agent tasks
- **Workflow Builder**: Visual workflow creation and management
- **Advanced Analytics**: Performance metrics and insights
- **Multi-theme Support**: Light/dark mode with custom themes
- **Responsive Design**: Works seamlessly on desktop and tablet devices
- **Real-time Notifications**: System alerts and task updates
- **API Integration**: Full integration with backend REST API

## 🏗️ Architecture

### Technology Stack

```
Frontend Framework: React 18.2.0
Routing: React Router v6.14.0
State Management: Context API + Hooks
Styling: Tailwind CSS 3.3.0
Animations: Framer Motion 10.12.0
HTTP Client: Axios 1.4.0
Charts: Chart.js 3.9.1
Real-time: Socket.io Client 4.6.1
UI Icons: React Icons 4.10.1
Data Tables: React Data Grid 7.0.0
Modals: Headless UI 1.7.4
Task Scheduling: React Big Calendar 1.8.5
```

### Directory Structure

```
frontend/
├── public/
│   ├── index.html              # HTML entry point
│   └── favicon.ico             # Application icon
├── src/
│   ├── index.jsx               # React entry point
│   ├── App.jsx                 # Main application component
│   ├── components/
│   │   ├── Sidebar.jsx         # Navigation sidebar
│   │   ├── Navbar.jsx          # Top navigation bar
│   │   ├── Notifications.jsx   # Notification system
│   │   └── ...
│   ├── pages/
│   │   ├── Dashboard.jsx       # Main dashboard
│   │   ├── TaskManager.jsx     # Task management
│   │   ├── Workflows.jsx       # Workflow management
│   │   ├── Analytics.jsx       # Analytics dashboard
│   │   └── Settings.jsx        # Settings page
│   ├── services/
│   │   ├── api.js              # API client configuration
│   │   └── taskService.js      # Task-related API calls
│   ├── hooks/
│   │   ├── useTaskManager.js   # Task management hook
│   │   └── useNotification.js  # Notification hook
│   ├── utils/
│   │   ├── constants.js        # App constants
│   │   └── formatters.js       # Data formatting utilities
│   ├── styles/
│   │   ├── globals.css         # Global styles
│   │   ├── theme.css           # Theme variables
│   │   └── components.css      # Component styles
│   └── context/
│       ├── ThemeContext.jsx    # Theme management
│       └── AppContext.jsx      # Global app context
├── package.json                # Dependencies and scripts
├── tailwind.config.js          # Tailwind configuration
├── postcss.config.js           # PostCSS configuration
└── FRONTEND_README.md          # This file
```

## 🚀 Quick Start

### Prerequisites

- Node.js 16.x or higher
- npm 8.x or yarn 3.x
- Backend server running (required for API integration)

### Installation

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment variables**:
   ```bash
   cp .env.example .env.local
   ```

   Edit `.env.local` with your backend API URL:
   ```
   REACT_APP_API_URL=http://localhost:8000
   REACT_APP_SOCKET_URL=http://localhost:8001
   ```

4. **Start development server**:
   ```bash
   npm start
   ```

   The application will open at `http://localhost:3000`

### Build for Production

```bash
npm run build
```

Optimized production build will be created in the `build/` directory.

## 📄 Available Scripts

### Development
```bash
npm start              # Start development server with hot reload
npm run dev           # Alternative development command
npm run test          # Run test suite
```

### Production
```bash
npm run build         # Create production build
npm run preview       # Preview production build locally
```

## 🎨 Component Architecture

### Layout Components

#### Sidebar.jsx
- Navigation menu with collapsible sections
- Active route highlighting
- User profile section
- Quick access shortcuts

#### Navbar.jsx
- Header with branding
- Theme toggle button
- User menu dropdown
- Search functionality

#### Notifications.jsx
- Toast notification system
- Priority-based styling
- Auto-dismiss functionality
- Action buttons support

### Page Components

#### Dashboard.jsx
- System metrics and KPIs
- Real-time status charts
- Recent activity feed
- Quick action buttons
- Task execution overview

#### TaskManager.jsx
- Task creation form
- Task list with filtering and sorting
- Task execution control
- Progress tracking
- Task history and logs

#### Workflows.jsx
- Visual workflow builder
- Workflow templates
- Execution scheduling
- Workflow history
- Performance analytics

#### Analytics.jsx
- Performance charts and graphs
- System health metrics
- Task success rates
- Resource utilization
- Custom date range filtering

#### Settings.jsx
- User preferences
- API key management
- Theme customization
- Integration settings
- Account management

## 🔌 API Integration

### API Service (`services/api.js`)

```javascript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add interceptors for authentication
api.interceptors.request.use(config => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

### Task Service (`services/taskService.js`)

```javascript
import api from './api';

export const taskService = {
  getTasks: () => api.get('/tasks'),
  createTask: (data) => api.post('/tasks', data),
  executeTask: (id) => api.post(`/tasks/${id}/execute`),
  getTaskStatus: (id) => api.get(`/tasks/${id}/status`),
  deleteTask: (id) => api.delete(`/tasks/${id}`),
};
```

## 🎯 State Management

### Context API Usage

#### ThemeContext.jsx
```javascript
const ThemeContext = createContext();

export const useTheme = () => useContext(ThemeContext);
```

#### AppContext.jsx
```javascript
const AppContext = createContext();

export const useApp = () => useContext(AppContext);
```

### Custom Hooks

#### useTaskManager.js
```javascript
export const useTaskManager = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  // Task management logic
};
```

## 🎨 Styling

### Tailwind CSS Configuration

The project uses Tailwind CSS v3 with custom configuration:

```javascript
// tailwind.config.js
module.exports = {
  content: [
    './src/**/*.{js,jsx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#3B82F6',
        secondary: '#8B5CF6',
        success: '#10B981',
        danger: '#EF4444',
      },
      animation: {
        fadeIn: 'fadeIn 0.3s ease-in-out',
        slideDown: 'slideDown 0.3s ease-in-out',
      },
    },
  },
  plugins: [],
};
```

### Theme Variables

Custom CSS variables for easy theme switching:

```css
:root {
  --primary-color: #3B82F6;
  --secondary-color: #8B5CF6;
  --background: #FFFFFF;
  --text-primary: #1F2937;
  --text-secondary: #6B7280;
  --border-color: #E5E7EB;
}

[data-theme='dark'] {
  --primary-color: #60A5FA;
  --secondary-color: #A78BFA;
  --background: #1F2937;
  --text-primary: #F9FAFB;
  --text-secondary: #D1D5DB;
  --border-color: #374151;
}
```

## 🔐 Security Considerations

### Authentication
- JWT token-based authentication
- Secure token storage in localStorage
- Automatic token refresh on expiry
- CORS configuration for backend

### Data Protection
- Sensitive data not logged to console
- HTTPS only in production
- Input validation on all forms
- XSS protection via React escaping

### Environment Variables
- Never commit `.env.local`
- Use `.env.example` as template
- Secure API key handling
- Production-specific secrets management

## 📊 Performance Optimization

### Code Splitting
- Lazy loading for route components
- React.lazy() for page components
- Dynamic imports for heavy libraries

### Bundle Optimization
- Tree shaking enabled
- CSS purging with Tailwind
- Image optimization
- Minification in production

### Runtime Performance
- Memoization with React.memo
- useCallback for function optimization
- Virtual scrolling for large lists
- Debouncing for search and filters

## 🧪 Testing

### Unit Tests
```bash
npm run test
```

### Test Coverage
```bash
npm run test -- --coverage
```

## 📦 Deployment

### Build Optimization
```bash
npm run build
```

### Deployment Options

#### Vercel
```bash
npm install -g vercel
vercel
```

#### Netlify
1. Connect repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `build`

#### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

## 🔧 Development Workflow

### Component Development

1. Create new component file in `src/components/`
2. Import necessary dependencies
3. Create functional component with hooks
4. Add PropTypes for type checking
5. Export component
6. Import and use in parent component

### Adding New Pages

1. Create page component in `src/pages/`
2. Add route in `App.jsx`
3. Add navigation link in `Sidebar.jsx`
4. Implement page-specific logic

## 🐛 Troubleshooting

### Common Issues

**Port 3000 already in use**:
```bash
lsof -ti:3000 | xargs kill -9
```

**Dependencies not installing**:
```bash
rm -rf node_modules package-lock.json
npm install
```

**API connection issues**:
- Verify backend server is running
- Check `.env.local` API URL configuration
- Review browser console for CORS errors

## 📚 Resources

- [React Documentation](https://react.dev)
- [React Router Docs](https://reactrouter.com)
- [Tailwind CSS](https://tailwindcss.com)
- [Framer Motion](https://www.framer.com/motion)
- [Axios Documentation](https://axios-http.com)

## 🤝 Contributing

Contribution guidelines for the frontend:

1. Create feature branch: `git checkout -b feature/name`
2. Follow ESLint rules
3. Write clean, documented code
4. Test components thoroughly
5. Submit pull request with description

## 📝 License

This project is part of the AI-Executive-Agent-Comet system.

## 📞 Support

For issues and questions, please open an issue in the GitHub repository.

---

**Last Updated**: 2024
**Version**: 1.0.0
**Status**: Active Development
