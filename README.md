# Python Automation Toolkit

A modular collection of lightweight, production-tested Python automation tools for system maintenance, file system organization, API health monitoring, and data pipelines.

## Modules

| Script | Purpose |
|---|---|
| `system_monitor.py` | Real-time CPU, RAM, and disk utilization logger with configurable alerts. |
| `file_organizer.py` | Automated directory sorting based on MIME types and custom extension rules. |
| `api_health_checker.py` | Concurrent HTTP endpoint prober with response time metrics and status alerts. |

## Quick Start

```bash
git clone https://github.com/4techno/python-automation-toolkit.git
cd python-automation-toolkit
pip install psutil requests
```

### 1. Run System Health Monitor

```bash
python scripts/system_monitor.py --interval 5 --threshold 85
```

### 2. Organize Downloads / Target Folder

```bash
python scripts/file_organizer.py --directory "~/Downloads" --dry-run
```

## Contributing

Contributions welcome! Submit issues or PRs with new automation recipes.

## License

MIT License.
