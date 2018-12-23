const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = val => {
  return val
    .toString()
    .toLowerCase()
    .trim()
    .replace(/&/g, '-and-') // replace & with '-and-'
    .replace(/[\s\W-]+/g, '-'); // replace spaces, non word chars, dashes with single dash
};

titleInput.addEventListener('keyup', event => {
  slugInput.setAttribute('value', slugify(titleInput.value));
});
