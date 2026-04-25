import sys

def patch():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Paste duplication
    old_paste = '''                    let isPasting = false;
                    window.addEventListener('paste', (e) => {
                        if (this.showAdmin && !isPasting) {
                            const items = (e.clipboardData || e.originalEvent.clipboardData).items;
                            for (let i = 0; i < items.length; i++) {
                                if (items[i].kind === 'file') {
                                    isPasting = true;
                                    const reader = new FileReader();
                                    reader.onload = (ev) => {
                                        this.form.images.push(ev.target.result);
                                        if (!this.form.mainImage) this.form.mainImage = ev.target.result;
                                        this.notify('Imagen añadida');
                                        setTimeout(() => isPasting = false, 500);
                                    };
                                    reader.readAsDataURL(items[i].getAsFile());
                                    break;
                                }
                            }
                        }
                    });'''
    new_paste = '''                    if (!window._pasteListenerAdded) {
                        window._pasteListenerAdded = true;
                        let isPasting = false;
                        window.addEventListener('paste', (e) => {
                            if (this.showAdmin && !isPasting) {
                                const items = (e.clipboardData || e.originalEvent.clipboardData).items;
                                for (let i = 0; i < items.length; i++) {
                                    if (items[i].kind === 'file') {
                                        isPasting = true;
                                        const reader = new FileReader();
                                        reader.onload = (ev) => {
                                            this.form.images.push(ev.target.result);
                                            if (!this.form.mainImage) this.form.mainImage = ev.target.result;
                                            this.notify('Imagen añadida');
                                            setTimeout(() => isPasting = false, 500);
                                        };
                                        reader.readAsDataURL(items[i].getAsFile());
                                        break;
                                    }
                                }
                            }
                        });
                    }'''
    content = content.replace(old_paste, new_paste)

    # 2. Product text spacing in card
    content = content.replace(
        'text-sm font-black text-white leading-tight uppercase tracking-tight line-clamp-2',
        'text-sm font-bold text-white leading-snug uppercase tracking-wide line-clamp-2 mt-1'
    )
    
    # Text spacing in modal
    content = content.replace(
        'text-2xl lg:text-3xl font-black font-display text-white tracking-tighter uppercase leading-[0.9]',
        'text-2xl lg:text-4xl font-black font-display text-white tracking-wide uppercase leading-tight'
    )

    # 3. Arrows in image (PC)
    old_showroom = '''                <div class="showroom-frame flex-1">
                    <div class="zoom-container" @mousemove="handleZoom($event)" @click="isZoomed = !isZoomed">
                        <img :src="activeProduct.images[activeIdx]" :class="{ 'scale-[2.5] cursor-zoom-out': isZoomed }" :style="isZoomed ? `transform-origin: ${zoomPos}` : 'transform-origin: center'" class="w-full h-full object-contain transition-transform duration-500 ease-out">
                    </div>
                    <template x-if="activeProduct.images.length > 1">
                        <div class="flex gap-4 mt-6">
                            <button @click="prevImg()" class="p-3 bg-white/5 rounded-full hover:bg-gold-500 hover:text-black transition-all shadow-xl"><i data-lucide="chevron-left" class="w-5 h-5"></i></button>
                            <div class="flex items-center gap-5 px-10">
                                <template x-for="(img, idx) in activeProduct.images" :key="idx"><div class="h-1.5 rounded-full transition-all duration-500" :class="activeIdx === idx ? 'w-8 bg-gold-500' : 'w-6 bg-white/10'"></div></template>
                            </div>
                            <button @click="nextImg()" class="p-3 bg-white/5 rounded-full hover:bg-gold-500 hover:text-black transition-all shadow-xl"><i data-lucide="chevron-right" class="w-5 h-5"></i></button>
                        </div>
                    </template>
                </div>'''
    new_showroom = '''                <div class="showroom-frame flex-1 relative flex items-center justify-center">
                    <template x-if="activeProduct.images.length > 1">
                        <button @click.stop="prevImg()" class="absolute left-4 z-10 p-3 bg-black/50 text-white rounded-full hover:bg-gold-500 hover:text-black transition-all shadow-xl backdrop-blur-sm"><i data-lucide="chevron-left" class="w-6 h-6"></i></button>
                    </template>
                    <div class="zoom-container w-full h-full absolute inset-0 flex items-center justify-center p-8" @mousemove="handleZoom($event)" @click="isZoomed = !isZoomed">
                        <img :src="activeProduct.images[activeIdx]" :class="{ 'scale-[2.5] cursor-zoom-out': isZoomed }" :style="isZoomed ? `transform-origin: ${zoomPos}` : 'transform-origin: center'" class="w-full h-full object-contain transition-transform duration-500 ease-out">
                    </div>
                    <template x-if="activeProduct.images.length > 1">
                        <button @click.stop="nextImg()" class="absolute right-4 z-10 p-3 bg-black/50 text-white rounded-full hover:bg-gold-500 hover:text-black transition-all shadow-xl backdrop-blur-sm"><i data-lucide="chevron-right" class="w-6 h-6"></i></button>
                    </template>
                    <template x-if="activeProduct.images.length > 1">
                        <div class="absolute bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-3 px-4 py-2 bg-black/50 backdrop-blur-sm rounded-full z-10 shadow-xl">
                            <template x-for="(img, idx) in activeProduct.images" :key="idx"><div class="h-1.5 rounded-full transition-all duration-500" :class="activeIdx === idx ? 'w-6 bg-gold-500' : 'w-2 bg-white/40'"></div></template>
                        </div>
                    </template>
                </div>'''
    content = content.replace(old_showroom, new_showroom)

    # 4. Google Maps error
    content = content.replace('href="https://maps.app.goo.gl/3X9vH5T6vL6"', 'href="https://www.google.com/maps/search/?api=1&query=-12.0851224,-76.8857306"')

    # 5. Mobile modal view scroll issues
    content = content.replace(
        'class="relative w-full max-w-7xl bg-premium-dark rounded-3xl shadow-2xl flex flex-col lg:flex-row max-h-[95vh] overflow-hidden border border-white/5 reveal"',
        'class="relative w-full max-w-7xl bg-premium-dark rounded-3xl shadow-2xl flex flex-col lg:flex-row max-h-[95vh] lg:overflow-hidden overflow-y-auto border border-white/5 reveal"'
    )
    content = content.replace(
        '<div class="w-full lg:w-3/5 h-full bg-premium-black relative border-r border-white/5 flex flex-col">',
        '<div class="w-full lg:w-3/5 min-h-[350px] lg:h-full bg-premium-black relative border-b lg:border-b-0 lg:border-r border-white/5 flex flex-col shrink-0">'
    )
    
    # 6. General Visual adjustments
    # Fix prices sizing and alignment in modal
    content = content.replace(
        '<div class="flex items-center gap-4">\n                        <span class="text-3xl lg:text-4xl font-black text-white tracking-tighter"',
        '<div class="flex items-center gap-4 mt-2">\n                        <span class="text-3xl lg:text-4xl font-black text-white tracking-wide"'
    )
    content = content.replace(
        '<span class="text-white/30 text-4xl line-through font-bold mt-6"',
        '<span class="text-white/40 text-xl lg:text-2xl line-through font-bold mt-2"'
    )
    
    # Fix sizes button font
    content = content.replace(
        'class="px-4 py-2 rounded-xl text-sm font-black text-lg border-2 transition-all"',
        'class="px-4 py-2 rounded-xl text-sm font-bold border-2 transition-all"'
    )
    
    # Fix Contact button
    content = content.replace(
        '<span class="font-black text-3xl uppercase tracking-tighter">Consultar Disponibilidad</span>',
        '<span class="font-black text-base lg:text-lg uppercase tracking-wide">Consultar Disponibilidad</span>'
    )
    content = content.replace(
        '<i data-lucide="message-circle" class="w-12 h-12"></i>',
        '<i data-lucide="message-circle" class="w-6 h-6"></i>'
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch()
print("Patch applied successfully.")
