from robusta.api import action, PodEvent, MarkdownBlock, TableBlock, FileBlock, Finding

@action
def report_and_isolate_suspicious_pod(event: PodEvent):
    pod = event.get_pod()
    if not pod:
        return

    pod_name = pod.metadata.name
    namespace = pod.metadata.namespace

    # Condition : Pod suspect (ex. crypto-miner)
    if "crypto-miner" in pod_name.lower():
        
        # 1️⃣ Créer un Finding personnalisé
        finding = Finding(
            title=f"🚨 Suspicious Pod Detected: {pod_name}",
            aggregation_key="suspicious_pods"
        )

        # 2️⃣ Ajouter enrichissements Markdown et tableau
        finding.add_enrichment([
            MarkdownBlock(f"Pod `{pod_name}` in namespace `{namespace}` seems suspicious."),
            TableBlock([["Pod Name", pod_name], ["Namespace", namespace]])
        ])

        # 3️⃣ Ajouter logs du pod
        try:
            logs = event.get_pod_logs()
            if logs:
                finding.add_enrichment([FileBlock("pod-logs.txt", logs)])
        except Exception:
            pass

        # 4️⃣ Ajouter le Finding à l’event pour l’envoyer vers Robusta UI / Slack / Webhook
        event.add_finding(finding)

        # 5️⃣ Supprimer le pod pour isolation immédiate
        pod.delete(grace_period_seconds=0)
