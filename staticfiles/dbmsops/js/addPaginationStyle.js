const ulPagination = document.querySelector('.pagination'); 
if(ulPagination){
  ulPagination.classList.add('justify-content-center');
  ulPagination.classList.add('pagination-sm');
  const listTags = ulPagination.children;
  for(let i=0; i<listTags.length; i++){
    listTags[i].classList.add('page-item');
    listTags[i].children[0].classList.add('page-link')
  }
}