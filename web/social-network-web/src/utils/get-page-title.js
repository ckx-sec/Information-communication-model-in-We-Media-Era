import defaultSettings from '@/settings'

const title = defaultSettings.title || '基于复杂网络的新型社交模型及信息传播分析平台'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
