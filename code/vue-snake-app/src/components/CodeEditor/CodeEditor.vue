<script setup lang="ts">
import { javascript } from '@codemirror/lang-javascript';
import { python } from '@codemirror/lang-python';
import { oneDark } from '@codemirror/theme-one-dark';
import { CSSProperties, computed } from 'vue';
import { Codemirror } from 'vue-codemirror';

export interface CodeEditorProps {
  modelValue: string;
  height?: CSSProperties['height'];
  tabSize?: number;
  language?: 'python' | 'javascript';
}

const props = defineProps<CodeEditorProps>();
const emit = defineEmits<{
  'update:modelValue': [value: string];
}>();

const code = computed({
  get() {
    return props.modelValue;
  },
  set(value) {
    emit('update:modelValue', value);
  },
});

const extensions = computed(() => [
  props.language === 'javascript' ? javascript() : python(),
  oneDark,
]);
</script>

<template>
  <codemirror
    :value="code"
    placeholder="Code goes here..."
    :style="{ height: props.height }"
    :autofocus="true"
    :indent-with-tab="true"
    :tab-size="props.tabSize ?? (language === 'javascript' ? 2 : 4)"
    :extensions="extensions" />
</template>
