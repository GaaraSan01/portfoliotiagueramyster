/*BAIXAR CV*/
const download_cv = document.getElementById('download_cv')

download_cv.addEventListener('click', () => {
    const fileName = 'curriculo.pdf'
    const filePath = './static/docs/' + fileName

    const link = document.createElement('a')
    link.href = filePath
    link.download = fileName
    document.body.appendChild(link)
    link.click()
})