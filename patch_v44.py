import sys

file_path = r"c:\Users\jeanp\.gemini\antigravity\scratch\ventas-zapatillas\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update version to 4.4
content = content.replace("v4.3", "v4.4")

# 2. Make modal wider
content = content.replace(
    '''<div class="relative w-full max-w-4xl bg-premium-dark rounded-3xl border-2 border-gold-500/20 shadow-2xl flex flex-col md:flex-row max-h-[95vh] overflow-y-auto reveal">''',
    '''<div class="relative w-full max-w-[90vw] lg:max-w-[85vw] bg-premium-dark rounded-3xl border-2 border-gold-500/20 shadow-2xl flex flex-col md:flex-row max-h-[95vh] overflow-y-auto reveal">'''
)

# 3. Make preview images larger inside modal
content = content.replace(
    '''<div :class="imageFormat === 'horizontal' ? 'aspect-[16/9] max-w-[550px]' : 'aspect-[3/4] max-w-[420px]'" class="w-full bg-premium-black rounded-xl border border-white/10 overflow-hidden relative shadow-[0_0_50px_rgba(251,191,36,0.15)] flex items-center justify-center transition-all duration-300">''',
    '''<div :class="imageFormat === 'horizontal' ? 'aspect-[16/9] max-w-[800px]' : 'aspect-[3/4] max-w-[500px]'" class="w-full bg-premium-black rounded-xl border border-white/10 overflow-hidden relative shadow-[0_0_50px_rgba(251,191,36,0.15)] flex items-center justify-center transition-all duration-300">'''
)

# 4. Fix SVG strikethrough (push down to y1=80%)
content = content.replace(
    '''<svg class="absolute inset-0 w-full h-full pointer-events-none" preserveAspectRatio="none"><line x1="-5%" y1="72%" x2="105%" y2="72%" stroke="rgba(255,255,255,0.4)" stroke-width="6"/></svg>''',
    '''<svg class="absolute inset-0 w-full h-full pointer-events-none" preserveAspectRatio="none"><line x1="-5%" y1="80%" x2="105%" y2="80%" stroke="rgba(255,255,255,0.4)" stroke-width="6"/></svg>'''
)
content = content.replace(
    '''<svg class="absolute inset-0 w-full h-full pointer-events-none" preserveAspectRatio="none"><line x1="-5%" y1="72%" x2="105%" y2="72%" stroke="rgba(255,255,255,0.4)" stroke-width="5"/></svg>''',
    '''<svg class="absolute inset-0 w-full h-full pointer-events-none" preserveAspectRatio="none"><line x1="-5%" y1="80%" x2="105%" y2="80%" stroke="rgba(255,255,255,0.4)" stroke-width="5"/></svg>'''
)

# 5. Fix Sizes centering (remove mt-1 and mt-1.5, use pb-1 to lift slightly)
content = content.replace(
    '''<span x-text="sz" class="leading-none mt-1.5"></span>''',
    '''<span x-text="sz" class="leading-none pb-1"></span>'''
)
content = content.replace(
    '''<span x-text="sz" class="leading-none mt-1"></span>''',
    '''<span x-text="sz" class="leading-none pb-1"></span>'''
)

# 6. Horizontal Template modifications
# Remove webkit line-clamp to show full review
content = content.replace(
    '''<p class="text-white/70 text-[30px] leading-[1.6] font-medium max-h-[150px] overflow-hidden" style="display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;" x-text="shareProduct?.description"></p>''',
    '''<p class="text-white/70 text-[35px] leading-[1.5] font-medium" x-text="shareProduct?.description"></p>'''
)

# Change Horizontal Template to 1920x1080 min-height layout to fit content
content = content.replace(
    '''<div id="story-template-horizontal" class="w-[1600px] h-[900px] bg-[#0c0c0c] flex p-16 box-border gap-16 font-sans relative">''',
    '''<div id="story-template-horizontal" class="w-[1920px] min-h-[1080px] h-max bg-[#0c0c0c] flex p-20 box-border gap-20 font-sans relative">'''
)
content = content.replace(
    '''<div class="w-[750px] h-full shrink-0 bg-white rounded-xl flex items-center justify-center p-4 relative overflow-hidden shadow-2xl border border-white/10">''',
    '''<div class="w-[900px] h-auto shrink-0 bg-white rounded-3xl flex items-center justify-center p-8 relative overflow-hidden shadow-2xl border border-white/10">'''
)

# Increase font sizes slightly in horizontal to match new 1920 width
content = content.replace(
    '''<h2 class="text-white text-[75px] font-black uppercase leading-[1.1] tracking-tight mb-10 break-words" x-text="shareProduct?.name"></h2>''',
    '''<h2 class="text-white text-[90px] font-black uppercase leading-[1.1] tracking-tight mb-10 break-words" x-text="shareProduct?.name"></h2>'''
)
content = content.replace(
    '''<div class="relative w-28 h-16 bg-[#1a1a1a] border border-white/10 rounded-xl">''',
    '''<div class="relative w-36 h-20 bg-[#1a1a1a] border border-white/10 rounded-2xl">'''
)
content = content.replace(
    '''<div class="absolute inset-0 flex items-center justify-center text-white text-[32px] font-bold">''',
    '''<div class="absolute inset-0 flex items-center justify-center text-white text-[40px] font-bold">'''
)

# Remove the Green button
content = content.replace(
    '''<div class="bg-[#25D366] text-white rounded-2xl py-6 px-10 flex items-center justify-center gap-4 shadow-lg w-max border border-white/20">
                        <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564c.173.087.289.129.332.202.043.073.043.423-.101.827z"/></svg>
                        <span class="text-[32px] font-black uppercase tracking-wide">CONSULTAR DISPONIBILIDAD</span>
                    </div>''',
    ''
)

# Increase Horizontal prices font size
content = content.replace(
    '''<span class="text-white text-[80px] font-black leading-none" x-text="'S/ ' + (shareProduct?.offerPrice || shareProduct?.originalPrice)"></span>''',
    '''<span class="text-white text-[120px] font-black leading-none" x-text="'S/ ' + (shareProduct?.offerPrice || shareProduct?.originalPrice)"></span>'''
)
content = content.replace(
    '''<span class="text-white/40 text-[50px] font-bold leading-none" x-text="'S/ ' + shareProduct?.originalPrice"></span>''',
    '''<span class="text-white/40 text-[65px] font-bold leading-none" x-text="'S/ ' + shareProduct?.originalPrice"></span>'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
