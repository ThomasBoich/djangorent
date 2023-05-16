let navs = document.querySelectorAll('.nav_')
let item = document.querySelectorAll('.task-menu li')
navs.forEach(e => {
    e.addEventListener('click', () => {
        navs.forEach(e=>{
            e.classList.remove('active')
        })
        e.classList.add('active')
    })
})

item.forEach((e) => {
    e.addEventListener('click', () => {
        item.forEach((i) => {
            i.classList.remove('menu-active')
        })
        e.classList.add('menu-active')
    })
})