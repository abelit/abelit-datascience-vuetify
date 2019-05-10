const randomElement = (arr = []) => {
  return arr[Math.floor(Math.random() * arr.length)];
};

const kebab =  (str) => {
  return (str || '').replace(/([a-z])([A-Z])/g, '$1-$2').toLowerCase();
};

const toggleFullScreen = () => {
  let doc = window.document;
  let docEl = doc.documentElement;

  let requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
  let cancelFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;

  if (!doc.fullscreenElement && !doc.mozFullScreenElement && !doc.webkitFullscreenElement && !doc.msFullscreenElement) {
    requestFullScreen.call(docEl);
  }
  else {
    cancelFullScreen.call(doc);
  }
};

/**
 * 设置浏览器头部标题
 */
const setTitle = function(title) {
  title = title ? `${title}` : 'DataAV'
  window.document.title = title + '-DataAV'
}


export default {
  randomElement,
  toggleFullScreen,
  kebab,
  setTitle
};