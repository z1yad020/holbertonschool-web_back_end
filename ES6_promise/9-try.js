export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue.push(mathFunction());
  } catch (e) {
    const ex = `${e.name}: ${e.message}`;
    queue.push(ex);
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
