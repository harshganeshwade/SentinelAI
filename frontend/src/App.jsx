import { NavLink, Route, Routes } from 'react-router-dom';

const navItems = [
  { path: '/', label: 'Dashboard' },
  { path: '/incidents', label: 'Incident Center' },
  { path: '/investigation', label: 'Investigation Chat' },
  { path: '/reports', label: 'Reports' },
  { path: '/settings', label: 'Settings' },
];

function Dashboard() {
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">SentinelAI Dashboard</h1>
      <p className="text-slate-600">AI-powered security incident investigation and response for Splunk.</p>
      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        <Card title="AI Incident Summary" description="Review alert explanations, severity, and business impact." />
        <Card title="Root Cause Analysis" description="Inspect probable attack vectors and confidence scores." />
        <Card title="MITRE Mapping" description="Map alerts to ATT&CK tactics and techniques." />
      </div>
    </div>
  );
}

function Card({ title, description }) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
      <h2 className="text-xl font-semibold">{title}</h2>
      <p className="mt-2 text-slate-600">{description}</p>
    </div>
  );
}

function Incidents() {
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Incident Center</h1>
      <p className="text-slate-600">Browse active incidents and drill into findings.</p>
      <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <p>Sample incident list will appear here once backend integration is complete.</p>
      </div>
    </div>
  );
}

function Investigation() {
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Investigation Chat</h1>
      <p className="text-slate-600">Ask natural-language questions and convert them into Splunk queries.</p>
      <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
        <p>Sample prompt: "Show failed logins from India"</p>
      </div>
    </div>
  );
}

function Reports() {
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Reports</h1>
      <p className="text-slate-600">Generate executive incident reports with impact and recommendations.</p>
    </div>
  );
}

function Settings() {
  return (
    <div className="space-y-4">
      <h1 className="text-3xl font-semibold">Settings</h1>
      <p className="text-slate-600">Configure Splunk connectivity, API keys, and environment settings.</p>
    </div>
  );
}

function App() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b border-slate-200 bg-white/90 backdrop-blur-lg">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
          <div className="text-2xl font-semibold">SentinelAI</div>
          <nav className="flex gap-4">
            {navItems.map((item) => (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `rounded-full px-4 py-2 text-sm font-medium transition ${
                    isActive ? 'bg-slate-900 text-white' : 'text-slate-600 hover:bg-slate-100'
                  }`
                }
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-6 py-8">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/incidents" element={<Incidents />} />
          <Route path="/investigation" element={<Investigation />} />
          <Route path="/reports" element={<Reports />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
