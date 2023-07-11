/** @type {import('eslint').Linter.Config} */
module.exports = {
  root: true,
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:vue/vue3-recommended',
    'plugin:tailwindcss/recommended',
    'plugin:import/recommended',
    'plugin:import/typescript',
    'plugin:prettier/recommended',
  ],
  parserOptions: {
    parser: '@typescript-eslint/parser',
    ecmaVersion: 'latest',
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  plugins: ['@typescript-eslint', 'sort-destructure-keys'],
  rules: {
    '@typescript-eslint/explicit-function-return-type': 'off',
    'import/namespace': 'off',
    'import/order': [
      'error',
      {
        alphabetize: {
          order: 'asc',
        },
        groups: [
          'builtin',
          'external',
          'internal',
          'parent',
          'sibling',
          'index',
          'object',
          'type',
        ],
        'newlines-between': 'always',
      },
    ],
    'sort-destructure-keys/sort-destructure-keys': 'error',
    'tailwindcss/no-custom-classname': 'off',
    'vue/multi-word-component-names': 'off',
    'vue/no-reserved-component-names': 'off',
    'vue/no-unused-components': 'warn',
  },
  settings: {
    'import/resolver': {
      typescript: {},
    },
  },
};
