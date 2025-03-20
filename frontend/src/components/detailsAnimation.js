function detailsAnimation(item) {
    document.getElementById('root').style.filter = 'blur(10px)'

    document.getElementById('block').style.zIndex = '2'
    document.getElementById('block').onclick = () => {
        document.getElementById('block').style.zIndex = '-1'
        document.getElementById('root').style.filter = 'blur(0)'
    }
}

export default detailsAnimation
