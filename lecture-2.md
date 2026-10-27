---
title: Lecture 2 Notes
permalink: /lecture-2/
---

<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<div id="content"></div>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
const loadMarkdown = (url) => {
  fetch(url)
    .then(r => r.text())
    .then(md => {
      const fixed = md
        .replace(/\$\$([\s\S]*?)\$\$/g, '\\[ $1 \\]')
        .replace(/\$([^\n$]+?)\$/g, '\\($1\\)');
      document.getElementById('content').innerHTML = marked.parse(fixed);
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    })
    .catch(err => {
      document.getElementById('content').innerHTML = '<p>Unable to load the original note file.</p>';
    });
};
loadMarkdown('https://raw.githubusercontent.com/rustedgy/statmech/main/leonard_susskind/statistical_mechanics_lecture_2_notes.md');
</script>
