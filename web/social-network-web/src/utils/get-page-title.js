import defaultSettings from '@/settings'

const title = defaultSettings.title || '基于多维网络模型的社交媒体信息传播可视化分析软件'

export default function getPageTitle(pageTitle) {
  if (pageTitle) {
    return `${pageTitle} - ${title}`
  }
  return `${title}`
}
