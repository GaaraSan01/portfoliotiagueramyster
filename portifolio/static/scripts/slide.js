/*SLIDE*/
const imagens = document.querySelectorAll('.img_slider img')
const navidatorSlider = document.querySelector('.nav_slider')
const arrow_right = document.getElementById('right')
const arrow_left = document.getElementById('left')

class SliderProjects{

    constructor(children, arrow_left, arrow_right, navigation){
        this.children = children,
        this.arrow_left = arrow_left,
        this.arrow_right = arrow_right
        this.nav = navigation
    }

    ocultImg(){
        const ListImagens = this.children
        ListImagens.forEach(element => {
            element.style.display = 'none'
        });
    }

    seeImg(){
        //Liste de imagens
        const ArrayList = this.children
        let itemList = 0
        //Button
        const radios = this.nav.querySelectorAll('input[type="radio"]')
        const button_left = this.arrow_left
        const button_right = this.arrow_right
        
        button_left.addEventListener('click', () => {
            this.ocultImg()
            itemList = (itemList + 1) % ArrayList.length
            radios[itemList].click()
        })
        button_right.addEventListener('click', () => {
            this.ocultImg()
            itemList = (itemList - 1 + ArrayList.length) % ArrayList.length
            radios[itemList].click()
        })

        radios.forEach((radio, index) => {
            radio.addEventListener('change', () => {
                this.ocultImg();
                itemList = index;
                ArrayList[itemList].style.display = 'block';
            })
        })

        radios[0].click()
        ArrayList[0].style.display = 'block'
    }

    insertRadios(){
        const ArrayList = this.children
        for(let i = 0; i < ArrayList.length; i++){
            const radios = document.createElement('input')
            radios.type = 'radio'
            radios.id = i.toLocaleString()
            radios.name = 'sliderRadios'
            radios.value = i;
            this.nav.appendChild(radios)
        }
    }

    init(){
        this.ocultImg()
        this.insertRadios()
        this.seeImg()
        
    }
}

const slider = new SliderProjects(imagens, arrow_left, arrow_right, navidatorSlider)
slider.init()