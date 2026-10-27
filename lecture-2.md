---
title: Lecture 2 Notes
permalink: /lecture-2/
---

<div id="content"></div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<script>
fetch('https://raw.githubusercontent.com/rustedgy/statmech/main/leonard_susskind/statistical_mechanics_lecture_2_notes.md')
  .then(r => r.text())
  .then(md => {
    document.getElementById('content').innerHTML = marked.parse(md);
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.typesetPromise();
    }
  })
  .catch(err => {
    document.getElementById('content').innerHTML = '<p>Unable to load the original note file.</p>';
  });
</script>
