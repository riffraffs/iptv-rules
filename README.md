# iptv-rules

合并后的 IPTV 规则集。域名规则在前，`IP-CIDR` 在后。同一份规则同时提供 Clash YAML，以及 Surge、Loon、小火箭共用的 list。

规则按列表顺序匹配。域名放在前面时，多数连接在域名阶段就命中，不必先解析 DNS 再逐条比对 IP。`IP-CIDR` 留在末尾，只在域名都未命中时才参与匹配。两份上游合成一份后，每个客户端只加载一个规则集，也避免同一条规则被匹配两次。

## 订阅

`@main` 由 jsDelivr 缓存，更新大约在提交后 12 小时内生效。

### Clash / OpenClash

类型 HTTP，行为 `classical`，格式 yaml。

```
https://cdn.jsdelivr.net/gh/riffraffs/iptv-rules@main/iptv_merged.yaml
```

```
https://raw.githubusercontent.com/riffraffs/iptv-rules/main/iptv_merged.yaml
```

### Surge / Loon / 小火箭

这三种客户端的规则集都是同一份 list：一行一条，`TYPE,值`，没有 `payload:`。

Surge：`RULE-SET` 指向下面的地址。  
Loon：远程规则填这个地址，策略组选 IPTV 使用的组。  
小火箭：`RULE-SET,地址,策略组`。

```
https://cdn.jsdelivr.net/gh/riffraffs/iptv-rules@main/iptv_merged.list
```

```
https://raw.githubusercontent.com/riffraffs/iptv-rules/main/iptv_merged.list
```

## 来源

规则来自这两个仓库，分别为G佬和C佬的分流规则，去重后合并：

- [marcuccilli/gary](https://github.com/marcuccilli/gary) 的 [`iptv_clash.yaml`](https://github.com/marcuccilli/gary/blob/main/iptv_clash.yaml)
- [marcuccilli/Cathy](https://github.com/marcuccilli/Cathy) 的 [`cathy_clash.yaml`](https://github.com/marcuccilli/Cathy/blob/main/cathy_clash.yaml)

GitHub Actions 每天北京时间早上 9 点拉取这两个文件，重新排序并提交 `iptv_merged.yaml` 和 `iptv_merged.list`。上游仓库大约在北京时间 8:20–8:45 更新。
