<template>
  <div>
    <title>{{ $t('index_page.page_title') }}</title>
    <ComponentList :list="componentMetadata" :title="$t('index_page.list_title')" sorting="alphabetical" has-favorite-button />
  </div>
</template>

<script setup lang="ts">
import ComponentList from '@/components/common/ComponentList.vue';
import { componentMetadata } from '@/constants/Information';
</script>