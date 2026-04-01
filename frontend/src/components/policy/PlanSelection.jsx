import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import toast from 'react-hot-toast';
import { policyApi } from '../../services/api';
import { Bot, MapPin, Zap, ArrowRight, Loader2, CloudRain, Sun, Wind } from 'lucide-react';

export default function PlanSelection() {
  const [plans, setPlans] = useState([]);
  const [loading, setLoading] = useState(true);
  const [purchasingId, setPurchasingId] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function loadPlans() {
      try {
         const data = await policyApi.getPlans();
         setPlans(data);
      } catch (err) {
         toast.error("Failed to load plans");
      } finally {
         setLoading(false);
      }
    }
    loadPlans();
  }, []);

  const handlePurchase = async (planId) => {
    setPurchasingId(planId);
    try {
       toast('Initiating secure payment...', { icon: '🔒', style: { background: '#1C1C28', color: '#fff'} });
       await policyApi.purchasePlan(planId);
       
       toast.success('Payment successful! Policy Active.', { style: { background: '#1C1C28', color: '#fff'}});
       navigate('/dashboard');
    } catch (err) {
       toast.error('Payment failed');
    } finally {
       setPurchasingId(null);
    }
  };

  if (loading) {
     return (
        <div className="flex items-center justify-center h-64">
           <div className="w-8 h-8 animate-spin rounded-full border-4 border-dark-border border-t-brand-500" />
        </div>
     );
  }

  // We highlight the 'Standard' plan as the primary focus to match the screenshot style
  const highlightedPlan = plans.find(p => p.id === 'standard') || plans[0];

  return (
    <div className="flex flex-col min-h-screen pb-24 space-y-6">
      <div className="flex items-center justify-between pb-2">
         <div>
            <h1 className="text-4xl font-extrabold tracking-tight text-white mb-2 font-display">
               Choose your <br /> cover
            </h1>
            <p className="text-sm text-gray-400">
               Personalised for your zone & this week's forecast
            </p>
         </div>
         {highlightedPlan.badge && (
            <div className="px-3 py-1.5 border border-gold-500/30 bg-gold-500/10 rounded-full flex items-center shadow-[0_0_15px_rgba(250,204,21,0.15)]">
               <div className="w-2 h-2 rounded-full bg-gold-400 mr-2 animate-pulse"></div>
               <span className="text-[10px] font-bold tracking-wider text-gold-400 uppercase">{highlightedPlan.badge}</span>
            </div>
         )}
      </div>

      {/* AI Risk Assessment Card */}
      <div className="p-5 border bg-dark-card border-dark-border rounded-3xl shadow-[0_0_30px_rgba(0,0,0,0.5)] relative overflow-hidden">
         <div className="absolute top-0 right-0 w-32 h-32 bg-gold-500/10 rounded-full blur-3xl -mr-16 -mt-16 pointer-events-none"></div>

         <div className="flex items-start justify-between mb-4 relative z-10">
            <div className="flex items-center">
               <div className="p-1.5 bg-brand-500/10 rounded-lg mr-3 shadow-sm border border-brand-500/20">
                  <Bot className="w-5 h-5 text-brand-500" />
               </div>
               <h3 className="font-bold text-gold-500 text-md">AI Risk Assessment</h3>
            </div>
            <span className="text-xs text-brand-400 mt-1 flex items-center bg-brand-500/10 px-2 py-0.5 rounded-full border border-brand-500/20"><MapPin className="w-3 h-3 mr-1"/> Bengaluru</span>
         </div>

         <div className="mb-4 flex items-end justify-between relative z-10">
            <span className="text-xs text-gray-500 uppercase tracking-widest font-semibold">Current Risk Score</span>
            <span className="text-3xl font-black text-gold-500 italic tracking-tighter leading-none">74</span>
         </div>
         
         <div className="flex h-1.5 rounded-full overflow-hidden bg-dark-border mb-6 relative z-10">
            <div className="w-[74%] bg-gradient-to-r from-brand-600 to-brand-400 shadow-[0_0_10px_rgba(239,68,68,0.5)]"></div>
         </div>

         {/* 7-Day Forecast Text Box */}
         <div className="mb-6 p-4 bg-dark-highlight border border-dark-border rounded-2xl relative z-10">
             <h4 className="flex items-center text-xs font-bold text-gray-300 uppercase tracking-wide mb-2">
               <CloudRain className="w-4 h-4 mr-1.5 text-blue-400"/>
               7-Day Prediction
             </h4>
             <p className="text-sm text-gray-400 leading-relaxed">
               <strong className="text-white">85% chance</strong> of severe waterlogging in your primary zones due to continuous monsoons. High expected impact on delivery times and earnings.
             </p>
         </div>

         <div className="flex gap-2 w-full overflow-x-auto no-scrollbar relative z-10">
            <div className="flex items-center px-3 py-1.5 bg-dark-bg/50 border border-dark-border/80 rounded-full shrink-0">
               <CloudRain className="w-3.5 h-3.5 text-blue-400 mr-1.5" />
               <span className="text-xs text-gray-300">Rain: High</span>
            </div>
            <div className="flex items-center px-3 py-1.5 bg-dark-bg/50 border border-dark-border/80 rounded-full shrink-0">
               <Sun className="w-3.5 h-3.5 text-brand-400 mr-1.5" />
               <span className="text-xs text-gray-300">Heat: Medium</span>
            </div>
            <div className="flex items-center px-3 py-1.5 bg-dark-bg/50 border border-dark-border/80 rounded-full shrink-0">
               <Wind className="w-3.5 h-3.5 text-purple-400 mr-1.5" />
               <span className="text-xs text-gray-300">AQI: Low</span>
            </div>
         </div>
      </div>

      {/* Plans List */}
      <div className="space-y-4">
         {plans.map(plan => (
            <div key={plan.id} className={`p-6 border bg-dark-card rounded-3xl transition-all ${plan.id === highlightedPlan.id ? 'border-brand-500/30 shadow-[0_4px_20px_-5px_rgba(239,68,68,0.15)]' : 'border-dark-border shadow-lg'}`}>
               <div className="flex justify-between items-start mb-6">
                  <div className="flex items-center">
                     <div className={`p-2 rounded-xl mr-4 ${plan.id === 'pro' ? 'bg-purple-500/20' : plan.id === 'standard' ? 'bg-brand-500/20' : 'bg-green-500/20'}`}>
                        <div className="text-xl">🌱</div>
                     </div>
                     <div>
                        <h3 className="text-xl font-bold text-white">{plan.name}</h3>
                        <p className="text-xs text-gray-400 mt-1">{plan.label}</p>
                     </div>
                  </div>
                  <div className="text-right flex flex-col items-end">
                     <span className="text-2xl font-black text-white italic tracking-tighter">₹{plan.aiPrice}</span>
                     <span className="text-xs text-gray-500 mt-0.5">per week</span>
                  </div>
               </div>
               <div className="pt-4 border-t border-dark-border flex justify-between items-center">
                  <span className="text-sm text-gray-400">Max payout: <strong className="text-green-500 font-bold">₹{plan.maxDaily}/week</strong></span>
                  {plan.id !== highlightedPlan.id && (
                     <button 
                        onClick={() => handlePurchase(plan.id)}
                        disabled={purchasingId !== null}
                        className="text-xs font-bold text-gray-300 hover:text-white px-4 py-2 bg-dark-highlight rounded-full"
                     >
                        Confirm
                     </button>
                  )}
               </div>
            </div>
         ))}
      </div>

      {/* Sticky Bottom Action Bar matching the screenshot */}
      <div className="fixed bottom-0 left-0 right-0 p-5 bg-dark-bg/95 backdrop-blur-xl border-t border-dark-border z-30 pb-safe pb-24 md:pb-6">
         <div className="max-w-4xl mx-auto flex flex-col space-y-4">
            <div className="flex justify-between items-center text-sm">
               <div>
                  <span className="text-gray-400 block mb-1">This week's premium</span>
                  <div className="flex items-baseline">
                     <span className="text-3xl font-black text-brand-500 italic tracking-tighter mr-2">₹{highlightedPlan.aiPrice}</span>
                     <span className="text-gray-500">/ 7 days</span>
                  </div>
               </div>
               <div className="text-right">
                  <span className="text-gray-400 block mb-1">You're covered up to</span>
                  <span className="text-xl font-bold text-green-500">₹{highlightedPlan.maxDaily}</span>
               </div>
            </div>

            <button
               onClick={() => handlePurchase(highlightedPlan.id)}
               disabled={purchasingId !== null}
               className="w-full py-4 rounded-2xl flex items-center justify-center font-bold text-lg text-white bg-gradient-to-r from-brand-600 to-brand-400 hover:from-brand-500 hover:to-brand-300 shadow-[0_4px_20px_-5px_rgba(239,68,68,0.4)] disabled:opacity-70 transition-all group"
            >
               {purchasingId === highlightedPlan.id ? (
                  <Loader2 className="w-6 h-6 animate-spin" />
               ) : (
                  <>
                     Activate Cover via UPI
                     <ArrowRight className="w-5 h-5 ml-2 transition-transform group-hover:translate-x-1" />
                  </>
               )}
            </button>
         </div>
      </div>
    </div>
  );
}
