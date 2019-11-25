function showARVR(){
    document.getElementById('liARVR').classList.add('currentCategory')
    document.getElementById('liCLASS').classList.remove('currentCategory')
    document.getElementById('liMISC').classList.remove('currentCategory')
    document.getElementById('liALL').classList.remove('currentCategory')
    
    document.getElementById('projectsARVR').style.display = "block"
    document.getElementById('projectsCLASS').style.display = "none"
    document.getElementById('projectsMISC').style.display = "none"
    document.getElementById('projectsALL').style.display = "none"
}
function showCLASS(){
    document.getElementById('liARVR').classList.remove('currentCategory')
    document.getElementById('liCLASS').classList.add('currentCategory')
    document.getElementById('liMISC').classList.remove('currentCategory')
    document.getElementById('liALL').classList.remove('currentCategory')
    
    document.getElementById('projectsARVR').style.display = "none"
    document.getElementById('projectsCLASS').style.display = "block"
    document.getElementById('projectsMISC').style.display = "none"
    document.getElementById('projectsALL').style.display = "none"
}
function showMISC(){
    document.getElementById('liARVR').classList.remove('currentCategory')
    document.getElementById('liCLASS').classList.remove('currentCategory')
    document.getElementById('liMISC').classList.add('currentCategory')
    document.getElementById('liALL').classList.remove('currentCategory')
    
    document.getElementById('projectsARVR').style.display = "none"
    document.getElementById('projectsCLASS').style.display = "none"
    document.getElementById('projectsMISC').style.display = "block"
    document.getElementById('projectsALL').style.display = "none"
}
function showALL(){
    document.getElementById('liARVR').classList.remove('currentCategory')
    document.getElementById('liCLASS').classList.remove('currentCategory')
    document.getElementById('liMISC').classList.remove('currentCategory')
    document.getElementById('liALL').classList.add('currentCategory')
    
    document.getElementById('projectsARVR').style.display = "none"
    document.getElementById('projectsCLASS').style.display = "none"
    document.getElementById('projectsMISC').style.display = "none"
    document.getElementById('projectsALL').style.display = "block"
}