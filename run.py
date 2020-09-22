from kaggle_environments import make
import datetime
import json
import os
import sys
import raine_force_best_agent

if __name__ == '__main__':
    PLAYERS = 4
    environment = make(
        environment='halite',
        configuration={'episodeSteps': 400},
        steps=[],
        debug=True
    )
    environment.reset(PLAYERS)
    functions = [raine_force_best_agent.agent_fn] * PLAYERS
    environment.run(functions[:PLAYERS])
    json_result = environment.render(mode='json')
    data = json.loads(json_result)
    reward = [data['steps'][-1][i]['reward'] for i in range(PLAYERS)]
    print(f'reward={reward}')
    t = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    json_file_path = f'replay_{t}.json'
    with open(json_file_path, 'w') as f:
        f.write(json_result)
    html_result = environment.render(mode='html')
    html_file_path = f'replay_{t}.html'
    with open(html_file_path, 'w') as f:
        f.write(html_result)
    print(f'output to {json_file_path} and {html_file_path}')

