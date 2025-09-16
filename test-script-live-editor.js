(() => {
    // Helpers
    const $ = (s, r=document) => r.querySelector(s);
    const setVal = (id, val) => { const el = $('#'+id); if (!el) return; el.value = val; el.dispatchEvent(new Event('input')); };
    const selectByValue = (id, val) => { const el = $('#'+id); if (!el) return; el.value = val; el.dispatchEvent(new Event('change')); };
    const selectMulti = (id, values) => {
      const el = $('#'+id); if (!el) return;
      Array.from(el.options).forEach(o => { o.selected = values.includes(o.value); });
      el.dispatchEvent(new Event('change'));
    };
  
    // Preamble
    setVal('sipNumber', '042');
    setVal('title', 'Composable SIP Framework: Authoring, Activation, and Live Validation');
    setVal('created', '2025-09-16');
    selectMulti('consideration', ['Governance', 'Technical', 'Economics']);
    selectByValue('type', 'Consensus (hard fork)'); // Live editor normalizes to “Consensus”
    // Leave Layer hidden (like SIP-021), or uncomment to set:
    // selectByValue('layer', 'Consensus (hard fork)');
    selectByValue('status', 'Draft');
    selectByValue('license', 'BSD-2-Clause');
  
    // Authors (star bullets)
    setVal('authors', [
      '* Jane Doe <jane@example.org>',
      '* John Smith <john@domain.tld>',
      '* Alice Example <alice@org.tld>'
    ].join('\n'));
  
    // Sign-off (hyphen bullets)
    setVal('signoff', [
      '- Rafael Cárdenas <rafael@hiro.so> (SIP Editor)',
      '- Brice Dobry <brice@hiro.so> (Technical CAB)',
      '- Jude Nelson <jude@stacks.org> (Steering Committee)'
    ].join('\n'));
  
    // Discussions (single line or blank)
    setVal('discussions', 'https://github.com/stacksgov/sips/discussions/4242');
  
    // Abstract (H1 in output)
    setVal('abstract', [
      'This SIP introduces a composable framework for SIP authoring with live validation,',
      'aiming to reduce formatting drift and accelerate activation readiness while preserving',
      'SIP-021-style canonical formatting.'
    ].join('\n'));
  
    // Introduction (H1 in output) — include inline markdown
    setVal('introduction', [
      'The current SIP authoring surfaces present fragmentation and repeated formatting fixes.',
      'This proposal streamlines:',
      '',
      '- Standardized preamble fields (no bold labels).',
      '- Live preview to enforce canonical spacing and headings.',
      '- Optional schema hooks for in-browser validation.',
      '',
      'Key terms: `tenure`, `Stacker`, and `Bitcoin finality` are preserved semantically.'
    ].join('\n'));
  
    // Specification (H1 in output) — include lists, code, table
    setVal('specification', [
      '## Components',
      '- Preamble builder',
      '- Section normalizer',
      '- Markdown serializer',
      '',
      '## Serialization Rules',
      '```txt',
      'Field lines:    `Label: Value`',
      'Authors:        star-bulleted list',
      'Sign-off:       hyphen-bulleted list',
      'Sections:       H1 top-level only (e.g., # Abstract)',
      'Spacing:        single blank line between blocks',
      '```',
      '',
      '## Example Table',
      '| Field | Required | Notes |',
      '|---|---:|---|',
      '| Title | Yes | ≤ 200 chars |',
      '| Type | Yes | “Consensus”, “Standard”, etc. |',
      '| License | Yes | BSD 2-Clause recommended |',
      '',
      '## Pseudocode',
      '```pseudo',
      'function buildPreamble(fields):',
      '  lines = ["# Preamble", ""]',
      '  for label,value in fields:',
      '    if value: lines.push(label + ": " + value, "")',
      '  return join(lines, "\\n").trim()',
      '```'
    ].join('\n'));
  
    // Related Work (H1) — references, links
    setVal('related', [
      '- SIP-000: Process & governance conventions',
      '- SIP-021: Formatting conventions and activation phases',
      '- Prior art: Live editors (Marked.js), schema-first pipelines'
    ].join('\n'));
  
    // Backwards Compatibility (H1)
    setVal('backcompat', [
      'Non-breaking to existing SIPs; only affects authoring ergonomics and formatting consistency.',
      'Activation rules remain SIP-specific and unchanged by this proposal.'
    ].join('\n'));
  
    // Activation (H1) — checklist
    setVal('activation', [
      'Activation steps:',
      '1. Pilot with authors in one cycle.',
      '2. CAB sign-off on formatting parity.',
      '3. Steering Committee vote to adopt as recommended authoring tool.'
    ].join('\n'));
  
    // Reference Implementation (H1)
    setVal('refs', [
      'https://github.com/stacksgov/sips',
      'https://github.com/stacks-network/stacks-core'
    ].join('\n'));
  
    // References (H1) — numeric list
    setVal('references', [
      '- [1] FROST: https://eprint.iacr.org/2020/852.pdf',
      '- [2] WSTS:  https://trust-machines.github.io/wsts/wsts.pdf',
      '- [3] SIP-021 (local): sips-main/sips/sip-021/sip-021-nakamoto.md'
    ].join('\n'));
  
    // Trigger live update and log results
    if (typeof updateLive === 'function') updateLive();
    const md = ($('#livePreview') && $('#livePreview').textContent) || (typeof buildMarkdown === 'function' ? buildMarkdown() : '');
    console.clear();
    console.log('--- Live Markdown (generated) ---\n');
    console.log(md);
  
    // Optional: click the floating copy button if present
    const sideBtn = $('#copySideBtn');
    if (sideBtn) sideBtn.click();
  })();