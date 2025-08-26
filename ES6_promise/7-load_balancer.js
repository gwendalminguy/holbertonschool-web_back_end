export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.any([chinaDownload, USDownload]).then((value) => { return value });
}
