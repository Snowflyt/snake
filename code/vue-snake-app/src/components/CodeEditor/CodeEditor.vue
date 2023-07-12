<script setup lang="ts">
import { javascript } from '@codemirror/lang-javascript';
import { oneDark } from '@codemirror/theme-one-dark';
import { ref, shallowRef } from 'vue';
import { Codemirror } from 'vue-codemirror';

import type { Events as CodemirrorEvents } from 'vue-codemirror';

const props = defineProps<{ code: string }>();
const emit = defineEmits<{
  (e: 'changeHandle', code: string): void;
}>();

const extensions = [javascript(), oneDark];

// Codemirror EditorView instance ref
const view = shallowRef();

const handleReady = ((payload) => {
  view.value = payload.view;

  return true;
}) satisfies CodemirrorEvents['ready'];

const handleChange = ((payload) => {
  //console.log('change', payload);
  emit('changeHandle', payload);
  return true;
}) satisfies CodemirrorEvents['change'];

const handleFocus = ((payload) => {
  console.log('focus', payload);

  return true;
}) satisfies CodemirrorEvents['focus'];

const handleBlur = ((payload) => {
  console.log('blur', payload);

  return true;
}) satisfies CodemirrorEvents['blur'];
</script>

<template>
  <codemirror
    :value="code"
    placeholder="Code goes here..."
    :style="{ height: '400px' }"
    :autofocus="true"
    :indent-with-tab="true"
    :tab-size="2"
    :extensions="extensions"
    @ready="handleReady"
    @change="handleChange"
    @focus="handleFocus"
    @blur="handleBlur" />
</template>
