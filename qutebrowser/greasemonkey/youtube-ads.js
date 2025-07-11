// ==UserScript==
// @name Skip YouTube Ads
// @description Skips ads in YouTube videos
// @run-at document-start
// @include *.youtube.com/*
// ==/UserScript==
document.addEventListener('load', () => {
    const btn = document.querySelector('.videoAdUiSkipButton,.ytp-ad-skip-button-modern');
    if (btn) { btn.click(); }
    const ad = [...document.querySelectorAll('.ad-showing')][0];
    if (ad) { document.querySelector('video').currentTime = 9999999999; }
}, true);
