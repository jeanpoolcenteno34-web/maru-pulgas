import sys

file_path = r"c:\Users\jeanp\.gemini\antigravity\scratch\ventas-zapatillas\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update version to 4.2
content = content.replace("v4.1", "v4.2")

# 2. Add 'imageFormat' to state. Look for `shareProduct: null, previewImage: null,`
content = content.replace(
    "shareProduct: null,",
    "shareProduct: null, imageFormat: 'vertical',"
)

# 3. Modal controls: add selector and change preview container
content = content.replace(
    '''<div class="flex flex-col items-center">
                    <div class="inline-flex items-center justify-center gap-2 px-4 py-2 bg-gold-500/10 border border-gold-500/20 text-gold-500 text-[11px] font-black tracking-widest uppercase rounded-full mb-6">
                        <i data-lucide="instagram" class="w-4 h-4"></i> Redes Sociales
                    </div>
                    <h2 class="text-4xl lg:text-5xl font-black text-white uppercase tracking-tighter leading-tight mb-4">Generador<br><span class="text-gold-500">Imágenes</span> <span class="text-lg text-white/20 align-top">v4.1</span></h2>
                    <p class="text-white/40 text-sm font-medium leading-relaxed max-w-sm">Crea al instante una imagen de alta conversión para historias de Instagram, Facebook o WhatsApp.</p>
                </div>''',
    '''<div class="flex flex-col items-center">
                    <div class="inline-flex items-center justify-center gap-2 px-4 py-2 bg-gold-500/10 border border-gold-500/20 text-gold-500 text-[11px] font-black tracking-widest uppercase rounded-full mb-6">
                        <i data-lucide="instagram" class="w-4 h-4"></i> Redes Sociales
                    </div>
                    <h2 class="text-4xl lg:text-5xl font-black text-white uppercase tracking-tighter leading-tight mb-4">Generador<br><span class="text-gold-500">Imágenes</span> <span class="text-lg text-white/20 align-top">v4.2</span></h2>
                    
                    <div class="flex gap-2 w-full max-w-sm mt-4 bg-white/5 p-1.5 rounded-xl border border-white/10">
                        <button @click="imageFormat = 'vertical'; previewImage = null; updatePreview()" :class="imageFormat === 'vertical' ? 'bg-gold-500 text-black shadow-lg scale-[1.02]' : 'text-white/60 hover:text-white'" class="flex-1 py-3 rounded-lg font-black uppercase text-[11px] tracking-widest transition-all">Vertical</button>
                        <button @click="imageFormat = 'horizontal'; previewImage = null; updatePreview()" :class="imageFormat === 'horizontal' ? 'bg-gold-500 text-black shadow-lg scale-[1.02]' : 'text-white/60 hover:text-white'" class="flex-1 py-3 rounded-lg font-black uppercase text-[11px] tracking-widest transition-all">Horizontal</button>
                    </div>
                </div>'''
)

content = content.replace(
    '''<div class="aspect-[3/4] w-full max-w-[420px] bg-premium-black rounded-xl border border-white/10 overflow-hidden relative shadow-[0_0_50px_rgba(251,191,36,0.15)] flex items-center justify-center">''',
    '''<div :class="imageFormat === 'horizontal' ? 'aspect-[16/9] max-w-[550px]' : 'aspect-[3/4] max-w-[420px]'" class="w-full bg-premium-black rounded-xl border border-white/10 overflow-hidden relative shadow-[0_0_50px_rgba(251,191,36,0.15)] flex items-center justify-center transition-all duration-300">'''
)

# 4. Fix Vertical Strikethrough to use inset flex (100% foolproof)
content = content.replace(
    '''                                <div class="relative inline-flex items-center justify-center">
                                    <span class="text-white/40 text-[70px] font-bold leading-none pb-1" x-text="'S/ ' + shareProduct?.originalPrice"></span>
                                    <div class="absolute w-[110%] h-[6px] bg-white/40 top-[50%] left-[-5%] -translate-y-1/2 rounded-full"></div>
                                </div>''',
    '''                                <div class="relative inline-flex items-center justify-center">
                                    <span class="text-white/40 text-[70px] font-bold leading-none" x-text="'S/ ' + shareProduct?.originalPrice"></span>
                                    <div class="absolute inset-0 flex items-center pointer-events-none">
                                        <div class="w-full h-[6px] bg-white/40 rounded-full scale-110"></div>
                                    </div>
                                </div>'''
)

# 5. Fix Vertical Sizes to use absolute inset
content = content.replace(
    '''                                <div class="w-36 h-[5.5rem] flex items-center justify-center bg-[#151515] border border-white/20 text-white text-[44px] font-bold rounded-[1.2rem]">
                                    <span class="-translate-y-[2px] leading-none text-center" x-text="sz"></span>
                                </div>''',
    '''                                <div class="relative w-36 h-[5.5rem] bg-[#151515] border border-white/20 rounded-[1.2rem]">
                                    <div class="absolute inset-0 flex items-center justify-center text-white text-[44px] font-bold">
                                        <span x-text="sz" class="leading-none"></span>
                                    </div>
                                </div>'''
)

# 6. Add story-template-horizontal right before or after story-template
horizontal_template = """
    <!-- Horizontal Template -->
    <div class="fixed top-0 left-0 w-0 h-0 overflow-hidden pointer-events-none z-[-1]">
        <div id="story-template-horizontal" class="w-[1600px] h-[900px] bg-[#0c0c0c] flex p-16 box-border gap-16 font-sans relative">
            <div class="w-[750px] h-full shrink-0 bg-white rounded-xl flex items-center justify-center p-12 relative overflow-hidden shadow-2xl border border-white/10">
                <img :src="shareProduct?.mainImage" class="w-auto h-auto max-w-full max-h-full object-contain" crossorigin="anonymous">
                <template x-if="shareProduct?.outOfStock">
                    <div class="absolute top-12 right-12 bg-red-600 text-white text-[40px] font-black px-10 py-4 rounded-full uppercase tracking-widest rotate-[15deg] shadow-xl border-4 border-white">
                        AGOTADO
                    </div>
                </template>
            </div>
            
            <div class="flex-1 flex flex-col justify-center">
                <span class="text-gold-500 text-[28px] font-black uppercase tracking-[0.2em] mb-4" x-text="shareProduct?.brand || 'ADIDAS'"></span>
                <h2 class="text-white text-[75px] font-black uppercase leading-[1.1] tracking-tight mb-10 break-words" x-text="shareProduct?.name"></h2>
                
                <template x-if="shareProduct?.sizes">
                    <div class="mb-10">
                        <h4 class="text-white font-bold text-[28px] uppercase tracking-[0.1em] mb-6 flex items-center gap-4">
                            <span class="w-4 h-4 rounded-full bg-gold-500"></span> TALLAS DISPONIBLES
                        </h4>
                        <div class="flex flex-wrap gap-4">
                            <template x-for="sz in (shareProduct?.sizes ? shareProduct.sizes.split(',').map(s=>s.trim()).filter(s=>s!=='') : [])" :key="sz">
                                <div class="relative w-28 h-16 bg-[#1a1a1a] border border-white/10 rounded-xl">
                                    <div class="absolute inset-0 flex items-center justify-center text-white text-[32px] font-bold">
                                        <span x-text="sz" class="leading-none"></span>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </template>
                
                <template x-if="shareProduct?.description">
                    <div class="mb-10">
                        <h4 class="text-white font-bold text-[28px] uppercase tracking-[0.1em] mb-6 flex items-center gap-4">
                            <span class="w-4 h-4 rounded-full bg-gold-500"></span> RESEÑA DEL CALZADO
                        </h4>
                        <p class="text-white/70 text-[30px] leading-[1.6] font-medium max-h-[150px] overflow-hidden" style="display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;" x-text="shareProduct?.description"></p>
                    </div>
                </template>
                
                <div class="mt-auto flex flex-col gap-10">
                    <div class="flex items-end gap-8">
                        <span class="text-white text-[80px] font-black leading-none" x-text="'S/ ' + (shareProduct?.offerPrice || shareProduct?.originalPrice)"></span>
                        <template x-if="shareProduct?.offerPrice && shareProduct?.offerPrice < shareProduct?.originalPrice">
                            <div class="relative inline-flex items-center">
                                <span class="text-white/40 text-[50px] font-bold leading-none" x-text="'S/ ' + shareProduct?.originalPrice"></span>
                                <div class="absolute inset-0 flex items-center pointer-events-none">
                                    <div class="w-full h-[5px] bg-white/40 rounded-full scale-110"></div>
                                </div>
                            </div>
                        </template>
                    </div>
                    
                    <div class="bg-[#25D366] text-white rounded-2xl py-6 px-10 flex items-center justify-center gap-4 shadow-lg w-max border border-white/20">
                        <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86s.274.072.376-.043c.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564c.173.087.289.129.332.202.043.073.043.423-.101.827z"/></svg>
                        <span class="text-[32px] font-black uppercase tracking-wide">CONSULTAR DISPONIBILIDAD</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

content = content.replace("<!-- FAB Admin -->", horizontal_template + "\n    <!-- FAB Admin -->")

# 7. Update JS logic for openShareGenerator, updatePreview, generateFullImage, copyImage
old_js = """                async openShareGenerator(p) {
                    this.shareProduct = p;
                    this.previewImage = null;
                    this.showShareModal = true;
                    this.$nextTick(() => lucide.createIcons());
                    
                    setTimeout(async () => {
                        try {
                            const canvas = await html2canvas(document.getElementById('story-template'), {
                                scale: 0.3, 
                                backgroundColor: '#050505',
                                logging: false
                            });
                            this.previewImage = canvas.toDataURL('image/jpeg', 0.8);
                        } catch(e) {
                            console.error(e);
                            this.notify("Error al generar vista previa");
                        }
                    }, 500);
                },"""

new_js = """                async openShareGenerator(p) {
                    this.shareProduct = p;
                    this.previewImage = null;
                    this.imageFormat = 'vertical';
                    this.showShareModal = true;
                    this.$nextTick(() => lucide.createIcons());
                    this.updatePreview();
                },
                updatePreview() {
                    this.previewImage = null;
                    setTimeout(async () => {
                        try {
                            const targetId = this.imageFormat === 'horizontal' ? 'story-template-horizontal' : 'story-template';
                            const canvas = await html2canvas(document.getElementById(targetId), {
                                scale: 0.3, 
                                backgroundColor: '#050505',
                                logging: false
                            });
                            this.previewImage = canvas.toDataURL('image/jpeg', 0.8);
                        } catch(e) {
                            console.error(e);
                            this.notify("Error al generar vista previa");
                        }
                    }, 500);
                },"""

content = content.replace(old_js, new_js)

# Update html2canvas targeting globally for generateFullImage and copyImage
content = content.replace(
    "document.getElementById('story-template')",
    "document.getElementById(this.imageFormat === 'horizontal' ? 'story-template-horizontal' : 'story-template')"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
