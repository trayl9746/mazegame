import matplotlib.pyplot as plt # type: ignore


def showperformance_metrics(player_metrics=None, ai_metrics=None):
    if player_metrics:
        print(f"Player - Steps: {player_metrics.get('steps', 'N/A')}, Time: {player_metrics.get('time', 'N/A')} seconds")
    if ai_metrics:
        print(f"AI - Steps: {ai_metrics.get('steps', 'N/A')}, Time: {ai_metrics.get('time', 'N/A')} seconds")

    labels = ['Steps', 'Time (s)']
    x = range(len(labels))

    if player_metrics and ai_metrics:
        player_data = [player_metrics['steps'], player_metrics['time']]
        ai_data = [ai_metrics['steps'], ai_metrics['time']]

        plt.bar(x, player_data, label="Player", color="blue")
        plt.bar(x, ai_data, label="AI", color="green", alpha=0.7)
        plt.xticks(x, labels)
        plt.ylabel("Values")
        plt.legend()
        plt.title("Player vs AI Performance Metrics")
        plt.show()
    elif ai_metrics:
        ai_data = [ai_metrics['steps'], ai_metrics['time']]
        plt.bar(x, ai_data, label="AI", color="green", alpha=0.7)
        plt.xticks(x, labels)
        plt.ylabel("Values")
        plt.legend()
        plt.title("AI Performance Metrics")
        plt.show()

