<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zyra | Next-Gen Branding Automation</title>

    <!-- React & ReactDOM -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <!-- Babel -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: {
                            DEFAULT: '#7C3AED', // Violet 600
                            light: '#A78BFA',
                            dark: '#5B21B6',
                            glass: 'rgba(124, 58, 237, 0.1)'
                        },
                        secondary: {
                            DEFAULT: '#DB2777', // Pink 600
                            light: '#F472B6',
                            dark: '#9D174D',
                        },
                        accent: {
                            DEFAULT: '#0EA5E9', // Sky 500
                        },
                        surface: {
                            50: '#F8FAFC',
                            100: '#F1F5F9',
                            900: '#0F172A',
                            800: '#1E293B',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                        display: ['Outfit', 'Inter', 'sans-serif'],
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                        'blob': 'blob 7s infinite',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        },
                        blob: {
                            '0%': { transform: 'translate(0px, 0px) scale(1)' },
                            '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
                            '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
                            '100%': { transform: 'translate(0px, 0px) scale(1)' },
                        }
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;700;800&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8FAFC;
        }

        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {
            font-family: 'Outfit', sans-serif;
        }

        .glass {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.5);
        }

        .glass-dark {
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(30, 41, 59, 0.5);
        }

        .glass-card {
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
        }

        .text-gradient {
            background: linear-gradient(135deg, #7C3AED 0%, #DB2777 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Smooth fade in */
        .fade-enter {
            opacity: 0;
            transform: translateY(10px);
        }

        .fade-enter-active {
            opacity: 1;
            transform: translateY(0);
            transition: opacity 300ms, transform 300ms;
        }
    </style>
</head>

<body class="text-slate-800 antialiased overflow-x-hidden">
    <div id="root"></div>

    <script type="text/babel">
        const { useState, useEffect, useMemo } = React;
        const { createRoot } = ReactDOM;

        // --- ICONS (Simple Wrapper for Lucide) ---
        // Since we can't easily import icons in CDN React, we'll create simple SVG components
        // mimicking Lucide for critical icons.

        const Icon = ({ path, className = "w-6 h-6" }) => (
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className} dangerouslySetInnerHTML={{ __html: path }} />
        );

        const icons = {
            menu: '<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>',
            x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
            sparkles: '<path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>',
            layoutDashboard: '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
            type: '<polyline points="4 7 4 4 20 4 20 7"/><line x1="9" x2="15" y1="20" y2="20"/><line x1="12" x2="12" y1="4" y2="20"/>',
            penTool: '<path d="m12 19 7-7 3 3-7 7-3-3z"/><path d="m18 13-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="m2 2 7.586 7.586"/><circle cx="11" cy="11" r="2"/>',
            heart: '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
            shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/>',
            logOut: '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
            user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
            rocket: '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>'
        };

        // --- COMPONENTS ---

        const Button = ({ children, onClick, variant = 'primary', className = '' }) => {
            const baseStyle = "px-6 py-3 rounded-xl font-bold transition-all transform active:scale-95 flex items-center justify-center gap-2";
            const variants = {
                primary: "bg-gradient-to-r from-primary to-secondary text-white shadow-lg shadow-primary/30 hover:shadow-primary/50",
                secondary: "bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 shadow-sm",
                ghost: "bg-transparent text-slate-600 hover:bg-slate-100",
                outline: "border-2 border-primary text-primary hover:bg-primary/5"
            };
            return (
                <button onClick={onClick} className={`${baseStyle} ${variants[variant]} ${className}`}>
                    {children}
                </button>
            );
        };

        const Input = ({ label, type = "text", placeholder, value, onChange }) => (
            <div className="mb-4">
                {label && <label className="block text-sm font-medium text-slate-700 mb-1.5">{label}</label>}
                <input
                    type={type}
                    placeholder={placeholder}
                    value={value}
                    onChange={onChange}
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-primary focus:ring-4 focus:ring-primary/10 outline-none transition bg-white/70 backdrop-blur-sm"
                />
            </div>
        );

        const Modal = ({ isOpen, onClose, children, title }) => {
            if (!isOpen) return null;
            return (
                <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
                    <div className="absolute inset-0 bg-slate-900/20 backdrop-blur-sm" onClick={onClose}></div>
                    <div className="relative bg-white/90 backdrop-blur-xl border border-white/50 w-full max-w-md p-8 rounded-3xl shadow-2xl animate-[float_0.3s_ease-out]">
                        <div className="flex justify-between items-center mb-6">
                            <h3 className="text-2xl font-bold">{title}</h3>
                            <button onClick={onClose} className="p-2 hover:bg-slate-100 rounded-full transition">
                                <Icon path={icons.x} className="w-5 h-5" />
                            </button>
                        </div>
                        {children}
                    </div>
                </div>
            );
        };

        // --- PAGES ---

        const LandingPage = ({ onGetStarted, onLogin }) => {
            return (
                <div className="min-h-screen">
                    <div className="absolute inset-0 overflow-hidden -z-10 pointer-events-none">
                        <div className="absolute top-0 left-1/4 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob"></div>
                        <div className="absolute top-0 right-1/4 w-96 h-96 bg-pink-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-2000"></div>
                        <div className="absolute -bottom-32 left-1/2 w-96 h-96 bg-blue-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-blob animation-delay-4000"></div>
                    </div>

                    {/* Navbar */}
                    <nav className="fixed w-full z-40 glass border-b border-white/20">
                        <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                            <div className="flex items-center gap-2">
                                <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-primary to-secondary flex items-center justify-center text-white font-bold text-xl shadow-lg shadow-primary/20">Z</div>
                                <span className="font-display font-bold text-2xl text-slate-800 tracking-tight">Zyra</span>
                            </div>
                            <div className="hidden md:flex items-center gap-8">
                                <a href="#features" className="text-slate-600 hover:text-primary font-medium transition">Features</a>
                                <a href="#how" className="text-slate-600 hover:text-primary font-medium transition">How it Works</a>
                                <button onClick={onLogin} className="text-slate-900 font-bold hover:text-primary transition">Login</button>
                                <Button onClick={onGetStarted}>Get Started</Button>
                            </div>
                        </div>
                    </nav>

                    {/* Hero */}
                    <section className="pt-40 pb-20 px-6 text-center">
                        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/60 border border-purple-100 text-primary text-sm font-semibold mb-8 shadow-sm">
                            <span className="flex h-2 w-2 rounded-full bg-primary animate-pulse"></span>
                            AI-Powered Branding Revolution
                        </div>
                        <h1 className="text-5xl md:text-7xl font-extrabold mb-6 tracking-tight text-slate-900 leading-[1.1]">
                            Create Your Brand Identity <br /> <span className="text-gradient">In Seconds, Not Weeks</span>
                        </h1>
                        <p className="text-xl text-slate-600 mb-10 max-w-2xl mx-auto leading-relaxed">
                            Zyra uses advanced multimodal AI to generate names, logos, content, and strategy—tailored to your unique brand personality.
                        </p>
                        <div className="flex flex-col sm:flex-row justify-center gap-4">
                            <Button onClick={onGetStarted} className="px-10 py-4 text-lg">Start Branding Now</Button>
                            <Button variant="secondary" className="px-10 py-4 text-lg">Watch Demo</Button>
                        </div>

                        {/* Social Proof / Stats */}
                        <div className="mt-20 max-w-5xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-4 p-8 glass-card rounded-3xl">
                            <div><div className="text-3xl font-bold text-slate-800">10k+</div><div className="text-slate-500 text-sm">Brands Created</div></div>
                            <div><div className="text-3xl font-bold text-slate-800">1.2M</div><div className="text-slate-500 text-sm">Assets AI-Gen</div></div>
                            <div><div className="text-3xl font-bold text-slate-800">4.9/5</div><div className="text-slate-500 text-sm">User Rating</div></div>
                            <div><div className="text-3xl font-bold text-slate-800">ZERO</div><div className="text-slate-500 text-sm">Agency Fees</div></div>
                        </div>
                    </section>

                    {/* Features */}
                    <section id="features" className="py-24 px-6 bg-white/50">
                        <div className="max-w-6xl mx-auto">
                            <h2 className="text-4xl font-bold text-center mb-16 text-slate-900">Why Zyra?</h2>
                            <div className="grid md:grid-cols-3 gap-8">
                                <div className="p-8 rounded-3xl bg-white shadow-xl shadow-slate-200/50 hover:-translate-y-2 transition duration-300">
                                    <div className="w-14 h-14 bg-purple-100 rounded-2xl flex items-center justify-center text-primary mb-6"><Icon path={icons.sparkles} /></div>
                                    <h3 className="text-xl font-bold mb-3">Multimodal AI</h3>
                                    <p className="text-slate-600">Generates text, visuals, and strategy simultaneously for a cohesive brand identity.</p>
                                </div>
                                <div className="p-8 rounded-3xl bg-white shadow-xl shadow-slate-200/50 hover:-translate-y-2 transition duration-300">
                                    <div className="w-14 h-14 bg-pink-100 rounded-2xl flex items-center justify-center text-secondary mb-6"><Icon path={icons.heart} /></div>
                                    <h3 className="text-xl font-bold mb-3">Personality Engine</h3>
                                    <p className="text-slate-600">Aligns every asset with psychological archetypes to resonate deeply with your audience.</p>
                                </div>
                                <div className="p-8 rounded-3xl bg-white shadow-xl shadow-slate-200/50 hover:-translate-y-2 transition duration-300">
                                    <div className="w-14 h-14 bg-blue-100 rounded-2xl flex items-center justify-center text-accent mb-6"><Icon path={icons.shield} /></div>
                                    <h3 className="text-xl font-bold mb-3">Ethical Branding</h3>
                                    <p className="text-slate-600">Built-in bias checks ensure your brand is inclusive and culturally sensitive globally.</p>
                                </div>
                            </div>
                        </div>
                    </section>

                    <footer className="py-12 text-center text-slate-500 bg-white">
                        <p>© 2026 Zyra Branding Systems. Crafted with AI.</p>
                    </footer>
                </div>
            )
        };

        const Dashboard = ({ user, onLogout }) => {
            const [activeTool, setActiveTool] = useState(null);
            const [result, setResult] = useState(null);
            const [loading, setLoading] = useState(false);

            const tools = [
                { id: 'name', name: 'Smart Namer', icon: icons.type, color: 'text-primary', bg: 'bg-purple-100', desc: 'Generate unique, available business names based on your industry.' },
                { id: 'logo', name: 'Logo Creator', icon: icons.penTool, color: 'text-secondary', bg: 'bg-pink-100', desc: 'Design professional vector logos in seconds.' },
                { id: 'content', name: 'Brand Voice', icon: icons.layoutDashboard, color: 'text-accent', bg: 'bg-blue-100', desc: 'Create taglines, mission statements, and social copy.' },
                { id: 'ethics', name: 'Ethics Check', icon: icons.shield, color: 'text-emerald-600', bg: 'bg-emerald-100', desc: 'Scan your branding for inclusivity and bias.' }
            ];

            const runTool = (toolId) => {
                setActiveTool(toolId);
                setResult(null);
                setLoading(true);

                // Simulate AI api call
                setTimeout(() => {
                    setLoading(false);
                    if (toolId === 'name') setResult(["OmniFlow Systems", "Zyra Tech", "NovaSphere", "Lumina Works"]);
                    if (toolId === 'logo') setResult("https://via.placeholder.com/150/7C3AED/FFFFFF?text=Zyra+Logo");
                    if (toolId === 'content') setResult("Empowering the future of digital creativity through automated intelligence.");
                    if (toolId === 'ethics') setResult({ score: 98, status: "Clean", message: "No bias detected. Content is inclusive." });
                }, 2000);
            };

            return (
                <div className="flex min-h-screen bg-slate-50">

                    {/* Sidebar */}
                    <div className="w-64 bg-white border-r border-slate-200 p-6 hidden md:flex flex-col justify-between fixed h-full z-20">
                        <div>
                            <div className="flex items-center gap-3 mb-10 text-primary">
                                <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white font-bold">Z</div>
                                <span className="font-bold text-2xl tracking-tight text-slate-900">Zyra</span>
                            </div>
                            <div className="space-y-2">
                                <button className="w-full flex items-center gap-3 px-4 py-3 bg-slate-100 text-slate-900 rounded-xl font-medium transition"><Icon path={icons.layoutDashboard} className="w-5 h-5" /> Dashboard</button>
                                <button className="w-full flex items-center gap-3 px-4 py-3 text-slate-500 hover:bg-slate-50 rounded-xl font-medium transition"><Icon path={icons.user} className="w-5 h-5" /> Profile</button>
                                <button className="w-full flex items-center gap-3 px-4 py-3 text-slate-500 hover:bg-slate-50 rounded-xl font-medium transition"><Icon path={icons.sparkles} className="w-5 h-5" /> My Brands</button>
                            </div>
                        </div>

                        <div className="p-4 bg-purple-50 rounded-2xl">
                            <div className="text-xs font-bold text-primary mb-1">PRO PLAN</div>
                            <div className="text-xs text-purple-700 mb-3">You have 850 credits left.</div>
                            <button className="w-full py-2 bg-white text-primary text-xs font-bold rounded-lg shadow-sm">Upgrade</button>
                        </div>
                    </div>

                    {/* Main Content */}
                    <div className="flex-1 md:ml-64 p-8">
                        {/* Header */}
                        <div className="flex justify-between items-center mb-10">
                            <div>
                                <h2 className="text-3xl font-bold text-slate-900">Dashboard</h2>
                                <p className="text-slate-500">Welcome back, {user.username}!</p>
                            </div>
                            <button onClick={onLogout} className="flex items-center gap-2 text-slate-500 hover:text-red-500 transition font-medium">
                                <Icon path={icons.logOut} className="w-5 h-5" /> Logout
                            </button>
                        </div>

                        {/* Recent Brands Widget */}
                        <section className="mb-10">
                            <div className="p-6 rounded-3xl bg-gradient-to-r from-primary to-secondary text-white shadow-xl shadow-pink-500/20 relative overflow-hidden">
                                <div className="relative z-10 flex justify-between items-center">
                                    <div>
                                        <h3 className="text-2xl font-bold mb-1">Continue Project "Solaris"</h3>
                                        <p className="text-white/80">Last edited 2 hours ago</p>
                                    </div>
                                    <Button variant="secondary">Open Studio</Button>
                                </div>
                                <div className="absolute top-0 right-0 w-64 h-64 bg-white opacity-10 rounded-full mix-blend-overlay filter blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
                            </div>
                        </section>

                        {/* Tools Grid */}
                        <h3 className="text-xl font-bold text-slate-800 mb-6">AI Brand Engine</h3>
                        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                            {tools.map(tool => (
                                <div key={tool.id} onClick={() => runTool(tool.id)} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 hover:shadow-lg hover:-translate-y-1 transition cursor-pointer group">
                                    <div className={`w-12 h-12 ${tool.bg} rounded-xl flex items-center justify-center ${tool.color} mb-4 group-hover:scale-110 transition`}>
                                        <Icon path={tool.icon} className="w-6 h-6" />
                                    </div>
                                    <h4 className="font-bold text-slate-900 mb-2">{tool.name}</h4>
                                    <p className="text-sm text-slate-500 leading-snug">{tool.desc}</p>
                                </div>
                            ))}
                        </div>

                        {/* Tool Result Area */}
                        {activeTool && (
                            <div className="glass-card p-8 rounded-3xl animate-in fade-in slide-in-from-bottom-4">
                                <div className="flex justify-between items-center mb-6">
                                    <h3 className="text-xl font-bold flex items-center gap-3">
                                        Generating with <span className="text-primary">{tools.find(t => t.id === activeTool).name}</span>
                                    </h3>
                                    <button onClick={() => setActiveTool(null)} className="text-slate-400 hover:text-slate-600"><Icon path={icons.x} /></button>
                                </div>

                                {loading ? (
                                    <div className="py-12 flex flex-col items-center justify-center text-center">
                                        <div className="w-12 h-12 border-4 border-primary border-t-transparent rounded-full animate-spin mb-4"></div>
                                        <p className="text-slate-500 animate-pulse">Analyzing industry trends & archetypes...</p>
                                    </div>
                                ) : (
                                    <div className="space-y-4">
                                        {activeTool === 'name' && (
                                            <div className="grid grid-cols-2 gap-4">
                                                {result.map((name, i) => (
                                                    <div key={i} className="p-4 bg-white rounded-xl border border-slate-100 font-bold text-center text-lg text-slate-800 hover:border-primary cursor-pointer transition">{name}</div>
                                                ))}
                                            </div>
                                        )}
                                        {activeTool === 'logo' && (
                                            <div className="flex flex-col items-center">
                                                <div className="w-48 h-48 bg-slate-100 rounded-full flex items-center justify-center mb-4 overflow-hidden border-4 border-white shadow-lg">
                                                    <span className="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">ZYRA</span>
                                                </div>
                                                <p className="text-sm text-slate-500">Vector Preview Generated</p>
                                            </div>
                                        )}
                                        {activeTool === 'content' && (
                                            <div className="p-6 bg-white rounded-xl border border-slate-200 italic text-slate-700 text-lg text-center">
                                                "{result}"
                                            </div>
                                        )}
                                        {activeTool === 'ethics' && (
                                            <div className="flex items-center gap-6 p-4 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-800">
                                                <div className="text-4xl font-bold">{result.score}%</div>
                                                <div>
                                                    <div className="font-bold">Passed Checks</div>
                                                    <div className="text-sm opacity-80">{result.message}</div>
                                                </div>
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        )}
                    </div>
                </div>
            )
        };

        const App = () => {
            const [view, setView] = useState('landing'); // landing, login, register, dashboard
            const [params, setParams] = useState(null);
            const [user, setUser] = useState(null);

            // Check session
            useEffect(() => {
                const saved = localStorage.getItem('zyra_user');
                if (saved) {
                    setUser(JSON.parse(saved));
                    setView('dashboard');
                }
            }, []);

            const handleLogin = (e) => {
                e.preventDefault();
                // Simulation
                const fakeUser = { username: 'AlexDesigner', plan: 'pro' };
                localStorage.setItem('zyra_user', JSON.stringify(fakeUser));
                setUser(fakeUser);
                setView('dashboard');
            };

            const handleLogout = () => {
                localStorage.removeItem('zyra_user');
                setUser(null);
                setView('landing');
            };

            return (
                <main className="relative">
                    {view === 'landing' && (
                        <LandingPage
                            onGetStarted={() => setView('register')}
                            onLogin={() => setView('login')}
                        />
                    )}

                    {view === 'login' && (
                        <div className="min-h-screen flex items-center justify-center p-6 bg-slate-50 relative overflow-hidden">
                            <div className="absolute inset-0 z-0">
                                <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30"></div>
                                <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-pink-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30"></div>
                            </div>
                            <div className="w-full max-w-md bg-white/80 backdrop-blur-xl p-10 rounded-3xl shadow-2xl relative z-10 border border-white">
                                <div className="text-center mb-10">
                                    <div className="inline-block p-3 rounded-2xl bg-gradient-to-tr from-primary to-secondary text-white mb-4 shadow-lg shadow-primary/30">
                                        <Icon path={icons.rocket} className="w-8 h-8" />
                                    </div>
                                    <h2 className="text-3xl font-bold text-slate-800">Welcome Back</h2>
                                    <p className="text-slate-500">Sign in to continue building your brand.</p>
                                </div>
                                <form onSubmit={handleLogin} className="space-y-6">
                                    <Input label="Email" placeholder="you@company.com" />
                                    <Input label="Password" type="password" placeholder="••••••••" />
                                    <Button className="w-full" onClick={handleLogin}>Sign In</Button>
                                </form>
                                <p className="mt-8 text-center text-slate-600">
                                    New to Zyra? <button onClick={() => setView('register')} className="text-primary font-bold hover:underline">Create Account</button>
                                </p>
                            </div>
                        </div>
                    )}

                    {view === 'register' && (
                        <div className="min-h-screen flex items-center justify-center p-6 bg-slate-50 relative overflow-hidden">
                            <div className="absolute inset-0 z-0">
                                <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30"></div>
                                <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-pink-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30"></div>
                            </div>
                            <div className="w-full max-w-md bg-white/80 backdrop-blur-xl p-10 rounded-3xl shadow-2xl relative z-10 border border-white">
                                <h2 className="text-3xl font-bold text-center mb-2">Start for Free</h2>
                                <p className="text-center text-slate-500 mb-8">No credit card required.</p>
                                <div className="space-y-4">
                                    <Input label="Company Name" placeholder="e.g. Acme Inc" />
                                    <Input label="Email" placeholder="you@company.com" />
                                    <Input label="Password" type="password" placeholder="••••••••" />
                                    <Button className="w-full" onClick={handleLogin}>Create Account</Button>
                                </div>
                                <p className="mt-8 text-center text-slate-600">
                                    Already have an account? <button onClick={() => setView('login')} className="text-primary font-bold hover:underline">Sign In</button>
                                </p>
                            </div>
                        </div>
                    )}

                    {view === 'dashboard' && user && (
                        <Dashboard user={user} onLogout={handleLogout} />
                    )}
                </main>
            );
        };

        const root = createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>

</html>