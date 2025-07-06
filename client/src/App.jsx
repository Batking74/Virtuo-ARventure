export default function App() {
  return (
    <>
      <h2></h2>
      <div className="demo">
        <model-viewer
          src="/images/lion.glb"
          auto-rotate
          camera-controls
          touch-action="pan-y"
          skybox-image="/images/background.png"
          ar></model-viewer>
      </div>
    </>
  );
}