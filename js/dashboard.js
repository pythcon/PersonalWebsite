function showResumeUpload(){
    document.getElementById('dashResumeContainer').style.display = "block"
    document.getElementById('dashProjectsContainer').style.display = "none"
    document.getElementById('dashRemoveProjectsContainer').style.display = "none"
}
function showProjectUpload(){
    document.getElementById('dashResumeContainer').style.display = "none"
    document.getElementById('dashProjectsContainer').style.display = "block"
    document.getElementById('dashRemoveProjectsContainer').style.display = "none"
}
function showProjectRemoval(){
    document.getElementById('dashResumeContainer').style.display = "none"
    document.getElementById('dashProjectsContainer').style.display = "none"
    document.getElementById('dashRemoveProjectsContainer').style.display = "block"
}