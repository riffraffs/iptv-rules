# iptv-rules

合并后的 Clash classical 规则集。域名规则在前，`IP-CIDR` 在后。

Clash 按列表顺序匹配。域名放在前面时，多数连接在域名阶段就命中，不必先解析 DNS 再逐条比对 IP。`IP-CIDR` 留在末尾，只在域名都未命中时才参与匹配。两份上游合成一份后，OpenClash 只加载一个规则集，也避免同一条规则被匹配两次。

## 订阅

OpenClash 规则集：类型 HTTP，行为 `classical`，格式 yaml。

jsDelivr（国内一般用这个）：

```
https://cdn.jsdelivr.net/gh/riffraffs/iptv-rules@main/iptv_merged.yaml
```

GitHub raw：

```
https://raw.githubusercontent.com/riffraffs/iptv-rules/main/iptv_merged.yaml
```

`@main` 由 jsDelivr 缓存，更新大约在提交后 12 小时内生效。

## 来源

规则来自这两个仓库，去重后合并：

- [marcuccilli/gary](https://github.com/marcuccilli/gary) 的 [`iptv_clash.yaml`](https://github.com/marcuccilli/gary/blob/main/iptv_clash.yaml)
- [marcuccilli/Cathy](https://github.com/marcuccilli/Cathy) 的 [`cathy_clash.yaml`](https://github.com/marcuccilli/Cathy/blob/main/cathy_clash.yaml)

GitHub Actions 每 6 小时拉取这两个文件，重新排序并提交 `iptv_merged.yaml`。
