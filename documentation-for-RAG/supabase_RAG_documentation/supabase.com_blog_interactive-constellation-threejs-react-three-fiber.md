---
url: "https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber"
title: "Coding the stars - an interactive constellation with Three.js and React Three Fiber"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Coding the stars - an interactive constellation with Three.js and React Three Fiber

04 Aug 2023

•

16 minute read

[![Francesco Sansalvadore avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffsansalvadore.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Francesco SansalvadoreEngineering](https://github.com/fsansalvadore)

![Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-constellation-breakdown-og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Every Launch Week is an opportunity for Supabase to experiment, try some spicy new designs, and dogfood our own technology. During our previous Launch Week we [took Generative AI for a spin](https://supabase.com/blog/designing-with-ai-midjourney). This time we decided to shoot for the stars.

For [Launch Week 8](https://supabase.com/launch-week/), we wanted to make the user-generated tickets a central piece of the launch week theme. To do this, we built a “constellation” of stars - an animated night sky where every user signup was represented as a star, in the form of an “8” shape.

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-early-design.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Early design

We could approach this animation in a few ways.

For example, animating the `stroke-dashoffset` on an SVG path, similar to [this](https://css-tricks.com/svg-line-animation-works/) example, was a good option, but it would have been difficult to randomize and change the shape at a later stage. Other approaches included 2D animation libraries, like [Framer Motion](https://www.framer.com/motion/animation/), [gsap](https://greensock.com/gsap/) or [PixiJS](https://pixijs.com/).

Ultimately we decided to take [Three.js](https://threejs.org/) for a spin using [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/getting-started/introduction) (R3F) giving us a more powerful toolset to enable us to achieve the best possible result.

Learning Three.js is not a walk in the park but R3F abstracted many of its complexities such as cameras and renderers, to name a few. If you're new to R3F, some of the core primitives they provide for a basic scene include:

- `Geometries`: used to create and define shapes
- `Materials`: manage the texture and color of objects
- `Mesh`: used to instantiate polygonal objects by combining a Geometry with a Material
- `Lights`: to shine bright like a diamond 💎🎵
- `Canvas`: where you define your R3F Scene

If you want to dive a little deeper, here are a few good resources we found to get a solid grasp on the topic:

- [I wish I knew this before using React Three Fiber](https://www.youtube.com/watch?v=DPl34H2ISsk) \- from our very own [Greg](https://twitter.com/ggrdson)
- [Three.js Journey](https://threejs-journey.com/) \- by [Bruno Simon](https://bruno-simon.com/)

## Setting up the scene [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#setting-up-the-scene)

In this article, we’re going to break down the steps to reproduce the Launch Week 8 animation using React Three Fiber in NextJs.

These are the dependencies we’ll need:

`
npm install three @react-three/fiber
`

If you’re using React 17, we’ll spare you the trouble of finding the last compatible R3F version:

`
npm install three @react-three/fiber@7.0.29
`

All we need for each particle is a circle geometry with a minimal amount of sides to minimize complexity.

`
import { useMemo } from 'react'
const Geometry = useMemo(() => () => <circleGeometry args={[1.5, 5]} />, [])
`

A basic standard material with a white color will do just fine. Using the AdditiveBlending module from `three` provides a more interesting touch when particles happen to overlap, making them shine brighter:

`
import { AdditiveBlending } from 'three'
const Material = () =>
useMemo(() => <meshStandardMaterial color="#ffffff" blending={AdditiveBlending} />, [])
`

Let’s put it together in an R3F `Canvas` element and wrap up the initial setup with an `ambientLight`, which will make objects visible, just as real light does:

`
import { useMemo } from 'react'
import { Canvas } from '@react-three/fiber'
import { AdditiveBlending } from 'three'
const Geometry = useMemo(
    () => () => <circleGeometry args={[1.5, 5]} />,
    []
)
const Material = () =>
    useMemo(
      () => (
        <meshStandardMaterial
          color="#ffffff"
          blending={AdditiveBlending}
        />
      ),
      []
    )
return (
<div style={{ width: 100vw, height: 100vh, background: "#000000" }}>
    <Canvas
      dpr={[1, 2]}
      camera={{ fov: 75, position: [0, 0, 500] }}
    >
      <ambientLight intensity={0.3} />
      <group>
        {particles?.map((particle, index) => (
          <mesh
            key={particle.username}
          >
            <Geometry />
            <Material />
          </mesh>
        ))}
      </group>
    </Canvas>
</div>
)
`

For more context, the `dpr` values help with pixelation issues and the `camera` \[0, 0, 500\] position means that the camera is moved 500 units back in the z-axis to actually see the center \[0,0,0\] of the scene.

One thing to note is that the R3F Canvas renders a transparent background, so in order to see the white particle, we need to set the background of the parent html element to a dark color.

We created a separate component for the Particle, which will later encapsulate the animation logic.

`
import React, { useRef } from 'react'
const Particle = ({ children }) => {
const particle = useRef(null)
return <mesh ref={particle}>{children}</mesh>
}
export default Particle
`

## Load users from Supabase [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#load-users-from-supabase)

You might have noticed we haven’t instantiated the particles yet. As we mentioned earlier, we wanted each particle to represent a ticket generated by a user and stored in the database. Let’s fetch the signups from the `tickets` table in our Supabase project (you might need to start your own Launch Week to fill your table):

`
const [particles, setParticles] = useState([])
const loadUsers = async () => {
return await supabase.from('lw8_tickets').select('*')
}
useEffect(() => {
const { data: users } = loadUsers()
setParticles(users)
}, [])
`

We updated the constellation in [realtime](https://supabase.com/realtime) whenever a new ticket was generated, but we’ll skip over this part to keep the article shorter. Since it’s all open-source, you can dive deeper [here](https://github.com/supabase/supabase/pull/16022/files#diff-e3298724d8ca571c732651658e388d70cafd90c4ceea99be8e5e7529ebb73a56R17-R52) if you wish.

## Animating the particles [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#animating-the-particles)

To move the particle around the screen we are going to leverage a few different concepts: _useFrame_ and _trigonometry_ 🤯

### useFrame [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#useframe)

Generally, the most optimal way to animate things in a browser viewport, using javascript, is by leveraging a method called [requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame), which _“tells the browser that you wish to perform an animation and requests that the browser calls a specified function to update an animation right before the next repaint.”_. R3F has a similar hook called [useFrame](https://docs.pmnd.rs/react-three-fiber/tutorials/basic-animations) that lets you execute code on every frame of Fiber's render loop. We’ll use this to change the position of the particles over time in a few moments.

### Using time as an animation variable [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#using-time-as-an-animation-variable)

We can extract time information from the useFrame `clock` parameter, to know how much time has elapsed in our application, and use that time to animate a value. Updating the `x` position with Math.sin() generates a horizontal oscillating movement. Multiply it with a `widthRadius` variable to customize the amplitude of the movement.

`
const particle = useRef(null)
const widthRadius = 100
const heightRadius = 100
useFrame(({ clock }) => {
    const timer = clock.getElapsedTime()
    particle.current.position.x = Math.sin(timer) * widthRadius
}
})
return <mesh ref={particle}>{children}</mesh>
`

![01-x-sine.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F01-x-sine.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Combine the previous horizontal movement with a `Math.cos()` on the `y` position to [draw a circle](https://en.wikipedia.org/wiki/Sine_and_cosine):

`
particle.current.position.y = Math.cos(timer) * heightRadius
`

![02-circle.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F02-circle.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Calculating the circumference we can get the time the x position takes to complete a full circle.

`
const circumference = (config.widthRadius * Math.PI * 2) / 100
`

When that happens, we can invert the cos sign on every other loop to obtain a basic 8 shape.

`
const isEven = Math.floor(timer / circumference) % 2 == 0
particle.current.position.x = Math.sin(timer) * widthRadius
particle.current.position.y = isEven
? Math.cos(timer) * heightRadius - heightRadius
: -Math.cos(timer) * heightRadius + heightRadius
`

![03-eight.gif](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2F03-eight.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

At this point, we played around with a number of parameters that made the animation more randomized and interesting.

For example, we randomized the speed and the delay of each particle:

`
const minSpeed = -0.3
const maxSpeed = 0.4
const speed = Math.random() * (minSpeed - maxSpeed) + maxSpeed
const delayOffsetFactor = 100
const delayOffset = Math.random() * delayOffsetFactor
[...]
const timer = clock.getElapsedTime() *** speed + delayOffset**
`

We offset the shape on the x-axis, to concentrate most of the particles in the core of the 8 shape and leave a smaller amount externally, by playing around with exponentials using Math.pow() in combination with some more randomization.

`
const xThickness = 7
const xRandomnessShape = 2.2
const xRandomness = 5
const pathOffset =
    Math.pow(
      Math.random() * xRandomnessShape,
      xRandomness - xRandomness / 2
    ) * xThickness
...
particle.current.position.x = Math.sin(timer) * widthRadius + pathOffset
`

Honestly, this was the result of a lot of playing and tweaking around, and we certainly didn’t hit the best possible result on the first try. Perhaps you want to take some time to experiment with the math - you might find even better and more configurable results.

## GUI playground [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#gui-playground)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-constellation-gui-demo.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

What really helped to visualize the shape, gather feedback, and decide on a final design was adding a GUI to play around with the values. You can try for yourself by appending `#debug` to the [supabase.com/launch-week#debu](http://supabase.com/launch-week#debug) [g](http://supabase.com/launch-weekdebug) url. Go crazy with it.

We used the [dat.gui](https://github.com/dataarts/dat.gui) library:

`
npm install dat.gui@0.7.9
`

Which needs to be loaded asynchronously, otherwise it raises a `window is not defined` error.

`
const init = async () => {
const dat = await import('dat.gui')
const gui = new dat.GUI()
}
useEffect(() => {
init()
}, [])
`

Then we prepared a `useParticlesConfig` hook with all the configuration wired up to the GUI. Whenever the GUI updated, we also updated react state.

`
import { useEffect, useState } from 'react'
import { range } from 'lodash'
let defaultConfig = {
particles: 1500,
widthRadius: 100,
topHeightRadius: 80,
bottomHeightRadius: 100,
xThickness: 7,
xRandomnessFactor: 2.2,
xRandomnessShape: 2.2,
xRandomness: 5,
yThickness: 20,
max_speed: 0.1,
min_speed: -0.1,
}
const useParticlesConfig = (): any => {
if (typeof window === 'undefined') return null
const hash = window.location.hash
const isDebugMode = hash.includes('#debug')
const [particles, setParticles] = useState(range(0, defaultConfig.particles))
const [config, setConfig] = useState(defaultConfig)
const handleSetConfig = (name, value) => {
    setConfig((prevConfig) => ({ ...prevConfig, [name]: value }))
}
const init = async () => {
    if (!isDebugMode) return
    const dat = await import('dat.gui')
    const gui = new dat.GUI()
    const particlesFolder = gui.addFolder('Particles')
    const shapeFolder = gui.addFolder('Shape')
    particlesFolder
      .add(config, 'particles')
      .min(1)
      .max(5000)
      .step(1)
      .onChange((value) => {
        handleSetConfig('particles', value)
        setParticles(range(0, value))
      })
    shapeFolder
      .add(config, 'widthRadius')
      .min(1)
      .max(200)
      .step(1)
      .onChange((value) => handleSetConfig('widthRadius', value))
    // add desired folders and parameters
    particlesFolder.open()
    shapeFolder.open()
}
useEffect(() => {
    init()
}, [])
return { config, handleSetConfig, particles, setParticles, isDebugMode }
}
export default useParticlesConfig
`

Here is the final code:

`
import React, { useMemo, useEffect, useState } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import { AdditiveBlending } from 'three'
import useParticlesConfig from './hooks/useParticlesConfig'
const ParticlesCanvas = () => {
if (typeof window === 'undefined') return null
const { config, particles } = useParticlesConfig()
const Geometry = useMemo(
    () => () => <circleGeometry args={[config.particlesSize, config.particlesSides]} />,
    []
)
const Material = () =>
    useMemo(
      () => (
        <meshStandardMaterial
          color={config.color}
          blending={config.particlesBlending ? AdditiveBlending : undefined}
        />
      ),
      []
    )
return (
    <div style={{ width: 100vw, height: 100vh, background: "#000000" }}>
      <Canvas
        dpr={[1, 2]}
        camera={{ fov: 75, position: [0, 0, 500] }}
      >
        <ambientLight intensity={config.lightIntensity} />
        <group>
          {particles?.map((particle, index) => (
            <Particle
              key={particle.username}
            >
              <Geometry />
              <Material />
            </Particle>
          ))}
        </group>
      </Canvas>
    </div>
)
}
const Particle = ({ children }: Props) => {
const particle = useRef(null)
const pathOffset =
    Math.pow(
      Math.random() * config.xRandomnessShape,
      config.xRandomness - config.xRandomness / 2
    ) * config.xThickness
const verticalRandomness = Math.random() * (config.yThickness - 1) + 1 - config.yThickness / 2
const speed = Math.random() * (config.min_speed - config.max_speed) + config.max_speed
const circumference = (config.widthRadius * Math.PI * 2) / 100
const delayOffsetFactor = 100
const delayOffset = Math.random() * delayOffsetFactor
useFrame(({ clock }) => {
    const timer = clock.getElapsedTime() * speed + delayOffset
    const isEven = Math.floor(timer / circumference) % 2 == 0
		// When the loop count is even, draw bottom 8 shape
    // if odd, draw top 8 shape
    particle.current.position.x = isEven
      ? Math.sin(timer) * config.widthRadius * config.widthRatio + pathOffset
      : Math.sin(timer) * config.widthRadius + pathOffset
    particle.current.position.y = isEven
      ? Math.cos(timer) * config.bottomHeightRadius -
        config.bottomHeightRadius +
        verticalRandomness
      : -Math.cos(timer) * config.topHeightRadius + config.topHeightRadius + verticalRandomness
})
return <mesh ref={particle}>{children}</mesh>
}
export default Particle
`

Now **_THAT’S_** how you create a new constellation ✨. Feel free to use the code and learnings to build your own.

## Conclusion [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#conclusion)

In this journey, you saw how to use Three.js and harness the power of React Three Fiber and creative experimentation to craft an animation. We leveraged trigonometry, animation hooks, and GUI playgrounds to build a "8" shape formed by user-generated stars.

If you loved this and the new [Launch Week 8](https://supabase.com/launch-week) branding, make sure to tune in on Monday at 09 AM PT as we unveil the full landing 💥

## More Supabase Design [\#](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber\#more-supabase-design)

- [Designing with AI: Generating unique artwork for every user](https://supabase.com/blog/designing-with-ai-midjourney)
- **[Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&t=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)

[Last post\\
\\
**Why we'll stay remote** \\
\\
5 August 2023](https://supabase.com/blog/why-supabase-remote)

[Next post\\
\\
**pgvector: Fewer dimensions are better** \\
\\
3 August 2023](https://supabase.com/blog/fewer-dimensions-are-better-pgvector)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Setting up the scene](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#setting-up-the-scene)
- [Load users from Supabase](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#load-users-from-supabase)
- [Animating the particles](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#animating-the-particles)
  - [useFrame](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#useframe)
  - [Using time as an animation variable](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#using-time-as-an-animation-variable)
- [GUI playground](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#gui-playground)
- [Conclusion](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#conclusion)
- [More Supabase Design](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber#more-supabase-design)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&text=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finteractive-constellation-threejs-react-three-fiber&t=Coding%20the%20stars%20-%20an%20interactive%20constellation%20with%20Three.js%20and%20React%20Three%20Fiber)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-early-design.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw8-constellation-breakdown%2Flw8-constellation-gui-demo.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)